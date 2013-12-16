from django.shortcuts import render
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from playerproject.apps.accounts.models import PPUser
from playerproject.apps.dashboard.models import (
    PPUserRecord,
    PPHockeyUserRecord,
    PPHockeyPlayerStats,
    PPPlayerStats, 
    PPHockeySkaterStats,
    PPHockeyGoalieStats
)
from playerproject.apps.dashboard.forms import PPHockeyUserRecordForm, PPHockeyGoalieStatsForm, PPHockeySkaterStatsForm, PPUserNoteForm, PPUserNote

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import inlineformset_factory


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


@login_required
def manager(request):
	playerrecords = PPHockeyUserRecord.objects.filter(recorded_by = request.user.id).order_by('time_modified')
	paginator = Paginator(playerrecords, 20) # Show 20 contacts per page
	page = request.GET.get('page')
	try:
		records = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
		records = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
		records = paginator.page(paginator.num_pages)

	return render(request,'dashboard/records.html', { 'records': records, 'paginator': paginator })


@login_required
def manager_add(request):
    if request.POST:
        form = PPHockeyUserRecordForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            item = form.save(commit=False)
            item.recorded_by = request.user
            item.save()

            return HttpResponseRedirect(reverse('dashboard_manager'))
        else:
            print('error')
            #failed
    else:
        form = PPHockeyUserRecordForm()

    return render(request, 'dashboard/recordadd.html', { 'form':form })


@login_required
def manager_compare(request, player_ids):
    id_list = player_ids.split('/')
    players = list(PPHockeyUserRecord.objects.filter(id__in=id_list))

    player1_basicinfo = players[0]
    player2_basicinfo = players[1]
    player1_is_goalie = players[0].is_goalie()
    player2_is_goalie = players[1].is_goalie()
    both_goalies = player1_is_goalie and player2_is_goalie
    one_goalie = player1_is_goalie or player2_is_goalie

    try:
        if player1_is_goalie:
            stat1 = PPHockeyGoalieStats.objects.get(pphockeyplayerstats_ptr_id = players[0].stats.id)
        else:
            stat1 = PPHockeySkaterStats.objects.get(pphockeyplayerstats_ptr_id = players[0].stats.id)
    except:
        stat1 = False

    try:
        if player2_is_goalie:
            stat2 = PPHockeyGoalieStats.objects.get(pphockeyplayerstats_ptr_id = players[1].stats.id)
        else:
            stat2 = PPHockeySkaterStats.objects.get(pphockeyplayerstats_ptr_id = players[1].stats.id)
    except:
        stat2 = False

    return render(request, 'dashboard/recordcompare.html' ,{'both_goalies': both_goalies,'one_goalie' : one_goalie,'p1_basicinfo' : player1_basicinfo, 'p2_basicinfo' : player2_basicinfo, 'stat1': stat1, 'stat2':stat2})


@login_required
def player_stats_update(request, player_id):
    record =  PPHockeyUserRecord.objects.get(id = player_id)
    stats = record.stats

    if request.POST:
        if record.is_goalie():
            form = PPHockeyGoalieStatsForm(request.POST)
        else:
            form = PPHockeySkaterStatsForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            item = form.save(commit=False)
            item.save()

            record.stats = item
            record.save()

            return HttpResponseRedirect(reverse('dashboard_manager'))
        else:
            print('error')
            #failed
    else:
        if record.is_goalie():
            form = PPHockeyGoalieStatsForm(instance=stats)
        else:
            form = PPHockeySkaterStatsForm(instance=stats)


    return render(request, 'dashboard/playeradd.html', { 'form':form } )

@login_required
def player(request, player_id):
    record =  PPHockeyUserRecord.objects.get(id = player_id)
    is_goalie = record.is_goalie()
    try:
        if is_goalie:
            stats = PPHockeyGoalieStats.objects.get(pphockeyplayerstats_ptr_id = record.stats.id)
        else:
            stats = PPHockeySkaterStats.objects.get(pphockeyplayerstats_ptr_id = record.stats.id)
    except:
        stats=False

    if request.POST:
        form = PPUserNoteForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            item = form.save(commit=False)
            item.save()
            record.notes.add(item)

            return HttpResponseRedirect('#notes')
        else:
            print('error')
            #failed
    else:
        form = PPUserNoteForm()

    return render(request, 'dashboard/player.html', {'basicinfo' : record, 'stats': stats, 'is_goalie': is_goalie, 'form':form} )



