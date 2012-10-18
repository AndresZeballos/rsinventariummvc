from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from invent.inventario.models import Articulo, Color, Producto, Talle, Local,\
    Categoria, Marca, Componente
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render_to_response('home.html')

@csrf_exempt
def consultar(request):
    cod = 0
    tal = 0
    col = 0
    loc = 0
    cat = 0
    mar = 0
    com = 0
    arts = []
    if request.method == "POST":
        cod = request.POST['codigo']
        tal = request.POST['talle']
        col = request.POST['color']
        loc = request.POST['local']
        cat = request.POST['categoria']
        mar = request.POST['marca']
        com = request.POST['componente']
        
        argums = {}
        if not cod == '0':
            argums["pk"] = cod
        if not mar == '0':
            argums["marca"] = mar
        if not cat == '0':
            argums["categoria"] = cat
        if not com == '0':
            argums["composiciones"] = com
        prod = Producto.objects.filter(**argums)
        
        for p in prod:
            ars = {"producto":p.id,}
            if not tal == '0':
                ars["talle"] = tal
            if not col == '0':
                ars["color"] = col
            if not loc == '0':
                ars["local"] = loc
            arts += list(Articulo.objects.filter(**ars))
        if arts == [] and argums == {}:
            arts = Articulo.objects.all()
        
    
    if arts == []:
        arts = Articulo.objects.all()
    cods = Producto.objects.all()
    tals = Talle.objects.all()
    cols = Color.objects.all()
    locs = Local.objects.all()
    cats = Categoria.objects.all()
    mars = Marca.objects.all()
    coms = Componente.objects.all()
    return render_to_response('inventario/index.html', {
            'articulos': arts,
            'codigos': cods,
            'talles': tals,
            'colores': cols,
            'locales': locs,
            'categorias': cats,
            'marcas': mars,
            'componentes': coms,
            
            'dicc':{
                1: ({'Codigo': cods}, cod),
                2: ({'Talle': tals}, tal),
                3: ({'Color': cols}, col),
                4: ({'Local': locs}, loc),
                5: ({'Categoria': cats}, cat),
                6: ({'Marca': mars}, mar),
                7: ({'Componente': coms}, com),
            },
        }, context_instance=RequestContext(request))
    

def detalle(request, art_id):
    a = get_object_or_404(Articulo, pk=art_id)
    return render_to_response('inventario/detail.html', {'articulo': a},
                               context_instance=RequestContext(request))

def stock(request):
    return render_to_response('inventario/stock.html')
    
