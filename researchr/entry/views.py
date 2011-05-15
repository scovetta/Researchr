from researchr.entry.models import Entry, EntryForm
from django.shortcuts import render_to_response

def ShowEntrySetAction(request):
    entries = Entry.objects.all()
    c = {'entry': entries[0]}
    return render_to_response('entry.html', c)

def ShowEntryAction(request, id):
    entry = Entry.objects.get(id=id)
    k = request.openid.sreg
    aa = request.session.items()
    assert False
    c = {'entry': entry}
    return render_to_response('entry.html', c)

def NewEntryAction(request):
    form = EntryForm()
    return render_to_response('new_entry.html', {'form' : form})