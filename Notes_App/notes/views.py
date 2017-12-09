from django.shortcuts import render
from UserMgnt.models import notes
from django.contrib.auth.models import User
from django_ajax.decorators import ajax
from notes.models import shared_notes
import json



# function to see all created and received notes.
def mynotes(request):
    
#      print("in mynotes view")
    
    context=dict()
    
    uname = request.GET['uname']
#     print("uname",uname)
    uid = User.objects.get(username=uname)
    m_nt = notes.objects.filter(owner_id_id = uid)
    all_users = User.objects.all()
    context['all_u']=all_users
        
    for i in m_nt:
#         print("notes",i.n_id)
        context['n_id']=i.n_id
    
    context['note']=m_nt
    context['username']=uname
    
    return render(request,'notes/mynotes.html',context)


# function to see all shared notes.
def s_notes(request):
    
    print("in shared notes view")
    context=dict()
    
    u_name = request.GET['u_name']
    u = User.objects.get(username=u_name)
    print("user id",u.id)
    sn = shared_notes.objects.filter(owner_id_id=u.id)
    context['share']=sn
    context['username']=u_name
    
    return render(request,'notes/shared_notes.html',context)


# function to which opens modal to update note.
def update_nt(request):
    
    print("in update page view")
    context=dict()
    
    id = request.GET['id']
    note = notes.objects.get(n_id = id)
    context['note_data']=note
    context['id']=id
    context['username']=note.n_owner
    return render(request,'notes/update.html',context)
     

# function which updates the note.
@ajax 
def update_note(request):
    
    print("in note data update")
    context=dict()
    n_nm = request.GET['n_name']
    n_con = request.GET['n_cnt']
    nid = request.GET['n_id']
    
    note = notes.objects.filter(n_id = nid).update(n_name=n_nm,n_content=n_con)
    print("note has been updated")
            
            
# function which deletes the note.  
@ajax        
def del_note(request):
    
    print("in del note")
    context=dict()
    
    id=request.GET['nid']        
    print("del id-",id)
    delt=notes(n_id=id).delete()
    print("note has been deleted")
    

# function to view the note.
def view_note(request):
    
    print("in view note fun") 
    
    context=dict()
        
    id = request.GET['id']
    note = notes.objects.get(n_id = id)
    context['note_data']=note
    context['id']=id
    context['username']=note.n_owner
    
    return render(request,'notes/view_note.html',context)


# function which opens modal to share note.
def share_page(request):
    
    context=dict()
    id = request.GET['id']
    note = notes.objects.get(n_id = id)
    context['note_data']=note
    all_users = User.objects.all()
    context['all_u']=all_users
    
    return render(request,'notes/share.html',context)


# function to share note with selected user
@ajax
def shared(request):
    
    print("in shared notes view")
    context=dict()
    
    s_usr=request.GET['usr']
    cnt = request.GET['n_cnt']
    
    data = json.loads(s_usr)

    nt = notes.objects.filter(n_content=cnt)
    for i in nt:
        owner_id=i.owner_id_id
        s_nt_owner=i.n_owner
        s_nt_id=i.n_id
        n_name = i.n_name
        mark_comp = i.mark_complete
        
    for i in data: 
    #   storing note in shared note table of specific user. 
        snt = shared_notes(n_id_id = s_nt_id , n_shrd_name=n_name , n_shrd_owner=s_nt_owner , n_shrd_with=i , owner_id_id=owner_id).save()
        
    for i in data:
    #   sharing note in notes table with specific user.  
        u = User.objects.get(username=i)
        uid=u.id
        note = notes(n_name=n_name ,n_owner=s_nt_owner,n_content=cnt,owner_id_id=uid,mark_complete=mark_comp)
        note.save()
     
        print("note has been shared")
        
 
 
# function which make note as mark as complete.   
@ajax    
def mark_comp(request):
    
    print("in mark view")
    context=dict()
    nid = request.GET['nid'] 
#     note = notes.objects.filter(n_id=nid)
#     for i in note:
#         n_name=i.n_name
#         print("n name-",n_name)   
#     n=notes.objects.filter(n_name=n_name).update(mark_complete=1)
    n=notes.objects.filter(n_id=nid).update(mark_complete=1)
    mark=1
    nid=nid

    return {"nid":nid,'n':n}
    print("note has been mark as complete")