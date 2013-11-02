from pyquery import PyQuery
import urlparse   
import libs.utils.constants as Constants
from lxml import etree
from apps.dztemplate.manager import get_template_as_string
from apps.dztemplate.manager import save_template
import urllib
import os

# MAIN ENGINE
class Converter:

	def __init__(self, template_name, file_name):
		template_string = get_template_as_string(template_name, file_name)
		self.html_obj = PyQuery(template_string.decode('utf-8'))
		self.file_name = file_name
		self.template_name = template_name
		self.location = Constants.S3_TEMPLATE_URL + template_name + '/'

	def run_upload_engine(self):
		self.insert_element_tags()
		self.commit_template()

	def run_edit_engine(self):
		self.replace_local_links() 
		self.include_scripts()

	def get_converted_html(self):
		final_html =  '<html>' + self.html_obj.html(method='html') + '</html>'
		return final_html.encode('utf-8')
 
	def commit_template(self):
		save_template(self.template_name, self.file_name, self.get_converted_html(), False)
 

	# INCLUDE SCRIPTS FUNCTIONS
	def include_scripts(self):  
		self.add_scripts(Constants.ENGINE_JS_INCLUDES) 
		self.add_css([Constants.FONTAWESOME_CSS_URL, Constants.ENGINE_CSS_URL])
	

	def add_css(self, sources): 
		src_str = "";
		for src in sources:
			src_str += '<link type="text/css" href="' + src + '" rel="stylesheet"></link>'

		self.html_obj('head').append(src_str) 

	def add_scripts(self, sources): 
		src_str = "";
		for src in sources:
			src_str += '<script type="text/javascript" src="' + src + '"></script>'

		self.html_obj('head').prepend(src_str)
 
 	# TAG FUNCTIONS
 	def insert_element_tags(self): 

 		self.dzid = 0
 		def assign_tag(i, this):

 			self.dzid += 1

 			if element_is_type(this, ['script', 'title', 'head', 'header', 'body', 'footer', 'link', 'style', 'meta', 'p', 'b', 'i', 'u', 'strong', 'em']):
 				return 

			this.set('dzid', str(self.dzid))

 		self.html_obj('*').each(assign_tag)

	# TEXT FUNCTIONS
	def update_text(self, target, value):
		elements = self.html_obj('*').filter('[dzid="' + target + '"]')  

		for e in elements:  
	 		pq = PyQuery(e)
	 		pq.empty()
	 		pq.append(value)
	 		return True

	 	return False
	 		 
	def new_text_element(self, text, ident):
		element = etree.Element('dztag')
		#element.set('dztype', 'text') 
		element.set('dzid', str(ident))
		element.text = text
		return element

	# COPY REMOVE FUNCTIONS
	def copy_element(self, target, new_id):
		elements = self.html_obj('*').filter('[dzid="' + target + '"]') 
		for e in elements:  
 			pq = PyQuery(e) 
 			result = pq.clone().insertAfter(pq)
 			result.attr('dzid', new_id)
 			children = result.find('[dzid]') 
 			for c in children:
 				new_id = str(int(new_id) + 1)
 				c.set('dzid', new_id)
 			return True

		return False

	def remove_element(self, target):
		elements = self.html_obj('*').filter('[dzid="' + target + '"]')
		for e in elements:  
 			pq = PyQuery(e) 
 			pq.remove()
 			return True

		return False

	# REPLACE LINK FUNCTIONS
	def replace_local_links(self):
		self.replace_link('src')
		self.replace_link('href')


	def replace_link(self, attr):
		elements = self.html_obj('*').filter('[' + attr + ']')

		for e in elements:
			value = e.get(attr);

			if is_absolute(value):
				continue

			file_name, file_extension = os.path.splitext(value)
			if file_extension == '' or file_extension.find('.html') > 0:
				continue

			value = self.location + value
			e.set(attr, value)
	  
	def update_link(self, target, value):
		elements = self.html_obj('*').filter('[dzid="' + target + '"]')  
		for e in elements:  
 			pq = PyQuery(e)
 			pq.attr('href', value)
 			return True
		return False

	# IMAGE FUNCTIONS
	def replace_image(self, target, image_name):
		elements = self.html_obj('*').filter('[dzid="' + target + '"]')  
		location = self.location + urllib.quote_plus(image_name)

		for e in elements:
			pq = PyQuery(e)
			if pq.eq(0).is_('img'):
				pq.attr('src', location)
			else:
				pq.css('background-image', 'url("' + location + '");')

			return location

		return None
		

# HELPER FUNCTIONS
def unique_text_id(num):
	return 'dztxt' + str(num)

def is_absolute(url):
	return bool(urlparse.urlparse(url.strip()).scheme)

def element_is_type(element,type_arr):
	for e_type in type_arr:
		if PyQuery(element).clone().empty().is_(e_type):
			return True
	return False


