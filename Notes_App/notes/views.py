from django.shortcuts import render
from UserMgnt.models import notes
from django.contrib.auth.models import User
from django_ajax.decorators import ajax
from notes.models import shared_notes
import json

# Create your views here.
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
    context['uname']=uname
    
    return render(request,'notes/mynotes.html',context)



def s_notes(request):
    
    print("in shared notes view")
    context=dict()
    
    u_name = request.GET['u_name']
    u = User.objects.get(username=u_name)
    print("user id",u.id)
    sn = shared_notes.objects.filter(owner_id_id=u.id)
    context['share']=sn
    
    return render(request,'notes/shared_notes.html',context)



def update_nt(request):
    
    print("in update page view")
    context=dict()
    
    id = request.GET['id']
    note = notes.objects.get(n_id = id)
    context['note_data']=note
    context['id']=id
    return render(request,'notes/update.html',context)
     

@ajax 
def update_note(request):
    
    print("in note data update")
    context=dict()
    n_nm = request.GET['n_name']
    n_con = request.GET['n_cnt']
    nid = request.GET['n_id']
        
#     print("update",nid)
    context['msg']=1
    note = notes.objects.filter(n_id = nid).update(n_name=n_nm,n_content=n_con)
    
    return render(request,'notes/update.html',context)
            
def delete_nt(request):
    
    print("in delete page view")
    context=dict()
    
    id = request.GET['id']
    note = notes.objects.get(n_id = id)
    context['note_data']=note
    context['id']=id
    return render(request,'notes/delete.html',context)
   
@ajax        
def del_note(request):
    
    print("in del note")
    context=dict()
    
    id=request.GET['nid']        
    print("del id-",id)
    delt=notes(n_id=id).delete()

    return render(request,'notes/delete.html',context) 




def view_note(request):
    
    print("in view note fun") 
    
    context=dict()
        
    id = request.GET['id']
    note = notes.objects.get(n_id = id)
    context['note_data']=note
    context['id']=id
    
    return render(request,'notes/view_note.html',context)


def share_page(request):
    
    context=dict()
    id = request.GET['id']
    note = notes.objects.get(n_id = id)
    context['note_data']=note
    all_users = User.objects.all()
    context['all_u']=all_users
    
    return render(request,'notes/share.html',context)

@ajax
def shared(request):
    
    print("in shared notes view")
    context=dict()
    
    s_usr=request.GET['usr']
    cnt = request.GET['n_cnt']
    
    data = json.loads(s_usr)
#     print("s usr-",data)
#     print("n cnt-",cnt)
    nt = notes.objects.filter(n_content=cnt)
    for i in nt:
        owner_id=i.owner_id_id
        s_nt_owner=i.n_owner
        s_nt_id=i.n_id
        n_name = i.n_name
        mark_comp = i.mark_complete
#     print("nameeeeeee-",n_name)
    for i in data:
#         print("iiiiii",i)   
    #   storing note in shared note table of specific user  
        snt = shared_notes(n_id_id = s_nt_id , n_shrd_name=n_name , n_shrd_owner=s_nt_owner , n_shrd_with=i , owner_id_id=owner_id,mark_complete=mark_comp).save()
        
    for i in data:
    #   sharing note with specific user  
        u = User.objects.get(username=i)
        uid=u.id
        note = notes(n_name=n_name ,n_owner=s_nt_owner,n_content=cnt,owner_id_id=uid,mark_complete=mark_comp)
        note.save()
     
        print("note is shared")
        
#     return render(request,'notes/shared_notes.html',context)
    
@ajax    
def mark_comp(request):
    
    print("in mark view")
    context=dict()
    nid = request.GET['nid']    
    n=notes.objects.filter(n_id=nid).update(mark_complete=1)
    mark=1
    nid=nid
#     need to pass all notes
#     return render(request,'notes/mynotes.html',context)
    return {"nid":nid,'n':n}