
from django.shortcuts import render,redirect

import biodata
from .models import ModelBiodata
from .forms import FormBiodata


# Create your views here.
def delete(request,delete_id):
    ModelBiodata.objects.get(id=delete_id).delete()
    return redirect("biodata:list")
def edit(request,edit_id):
    biodata_edit =  ModelBiodata.objects.get(id=edit_id)
    data = {
        'nama_depan':biodata_edit.nama_depan,
        'nama_belakang':biodata_edit.nama_belakang,
        'jenis_kelamin':biodata_edit.jenis_kelamin,
        }
    if request.method == 'POST':
        if biodata_edit.is_valid():
            biodata_edit.save()
            return redirect ('biodata:list')
    formbiodata = FormBiodata(request.POST or None, initial= data, instance=biodata_edit)
    context = {
        "title" : "MASUKAN BIODATA",
        "formbiodata": formbiodata
    }
    return render(request,'biodata/create.html',context)

def create(request):
    formbiodata = FormBiodata(request.POST or None)
    if request.method == 'POST':
        if formbiodata.is_valid():
            formbiodata.save()
        return redirect ('biodata:list')
    context = {
        "title" : "MASUKAN BIODATA",
        "formbiodata": formbiodata
    }
    return render(request,'biodata/create.html',context)
def list(request):
    modelbiodata = ModelBiodata.objects.all()
    context = {
        'title':'List peserta',
        'modelbiodata' : modelbiodata
    }
    return render(request,'biodata/list.html',context)
