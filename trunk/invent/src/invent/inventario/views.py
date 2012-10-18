from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from invent.inventario.models import Articulo, Color, Producto, Talle, Local,\
    Categoria, Marca, Componente
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render_to_response('home.html')

def consultar(request):
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
                1: ({'Codigo': cods}, 0),
                2: ({'Talle': tals}, 0),
                3: ({'Color': cols}, 0),
                4: ({'Local': locs}, 0),
                5: ({'Categoria': cats}, 0),
                6: ({'Marca': mars}, 0),
                7: ({'Componente': coms}, 0),
            }
        }, context_instance=RequestContext(request))
    

def detalle(request, art_id):
    a = get_object_or_404(Articulo, pk=art_id)
    return render_to_response('inventario/detail.html', {'articulo': a},
                               context_instance=RequestContext(request))

@csrf_exempt
def filtrar(request):
    print request
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
    
    art = []
    for p in prod:
        ars = {"producto":p.id,}
        if not tal == '0':
            ars["talle"] = tal
        if not col == '0':
            ars["color"] = col
        if not loc == '0':
            ars["local"] = loc
        art += list(Articulo.objects.filter(**ars))
    if art == [] and argums == {}:
        art = Articulo.objects.all()
    
    cods = Producto.objects.all()
    tals = Talle.objects.all()
    cols = Color.objects.all()
    locs = Local.objects.all()
    cats = Categoria.objects.all()
    mars = Marca.objects.all()
    coms = Componente.objects.all()
    return render_to_response('inventario/index.html', {
            'articulos': art,
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
    
def stock(request):
    return render_to_response('inventario/stock.html')
    
