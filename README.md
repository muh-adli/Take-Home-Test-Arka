# Take Home Test Arka

## How to run

make sure you have Python 3.8 or latest to run the following repo

### install python environment 

run this command on Powershell / terminal:

```powershell
python -m venv .venv
```

this code will make virtual environment to make sure its dependencies separated with your computer environment

### activate environment and install requirements.txt

to activate the virtual environment use this command on your powershell, or you can alternatively activate with activate scripts in scripts folder under .venv

```powershell
.venv\scripts\activate
```

after activating virtual environment, you can continue to install the requirements with this command

```python
pip install -r requirements.txt
```

wait for some time because without a dependencies the program might found some trouble

## Inventory API

### Initialize django ORM and DRF

based on Django and DRF documentation you should make django by following command:
`django-admin startproject InventoryAPI .`
it will initialize project named Inventory API on folder, then you can run `django-admin startapp API` to make API django app to make
an application named API

after that you could configure setting.py to set-up some html templates, add apps and 3<sup>rd</sup> party library into INSTALLED_APPS variable, and etc


### User, Product, Clients table

to build the table as assignment needs, i'm building model at models.py on API django app

```python
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

class Client(models.Model):
    service_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    contract_value = models.IntegerField()
```

so first building models, tables, column, and its options that meets the requirement, then run migration to make django apply to database

For the user table, i used default django user table as it has build-in security features, but if user table is needed, this code will provide the table

```python
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

class Client(models.Model):
    service_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    contract_value = models.IntegerField()
```

as you can see, it has format

```python
class Name(models.Models):
    Column = models.whatField(options)
```

you could add as the required table, column, and option on the column as needed

to apply models that you build into database, you could run the migration by run `manage.py migrate` command

```py
python InventoryAPI/manage.py migrate
```

### JSON, REST, and XML APIs

for the API you can run django by run manage.py with runserver command

```python
python InventoryAPI/manage.py runserver
```

wait while system checking is running, after chekcing the server will start. By default the server will start at
```http://127.0.0.1:8000/```

then you can open the homepage by opening the web then you can choose which API you'd like to see. or alternatively, you can use this links
|   |   |   |
|:---:|:---:|:---:|
|__[JSON](http://127.0.0.1:8000/api/v1/inventory/json/)__| __[REST](http://127.0.0.1:8000/api/v1/inventory/rest/)__ | __[XML](http://127.0.0.1:8000/api/v1/inventory/xml/)__ |

you can see the code that runs JSON, REST, and XML on the views.py under API folder

#### JSON

```python
def inventoryJson(request):
    start = datetime.now()
    products_qs = Product.objects.values('product_id', 'product_name', 'description', 'price')
    end = datetime.now()
    delta = end - start
    print("Inventory JSON qs: ", round(delta.total_seconds(), 3), "s")
    return JsonResponse(list(products_qs), safe=False)
```
For the JSON API, you have to retrieve the data from the database that named `product_qs` or for product query set. It will collect Product models as an object with column based on you set on values. then it will return as JSON reponse in a list.

as you can see there is start, end, and delta variable with print that print `"Inventory JSON qs: "`. the variables collect time to measure the API elapsed time.


#### Rest

```python
class inventoryRest(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        start = datetime.now()
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        end = datetime.now()
        delta = end - start
        print("Inventory REST qs: ", round(delta.total_seconds(), 3), "s")
        return Response(serializer.data)
```

As you can see it is not function but class. This class define Django Rest Framework (DRF) viewset that extends Model, providing features for CRUD operations.

for the core viewset is Product models in queryset variables, so viewset has template to get the query based on queryset. then serializer_class that build based on what column you expected on the output.

<b>serializer.py</b>
```python
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```
this serializer will serialize all column on Prodcut model.

and the list function is a custom to measure the time taken on the API


#### XML

```python
def inventoryXml(request):
    start = datetime.now()
    products_qs = Product.objects.all()

    root = Element('products')
    for product in products_qs:
        product_element = SubElement(root, 'product')
        SubElement(product_element, 'product_id').text = str(product.product_id)
        SubElement(product_element, 'product_name').text = product.product_name
        SubElement(product_element, 'description').text = product.description
        SubElement(product_element, 'price').text = str(product.price)
    
    xml_string = tostring(root, encoding='utf-8').decode('utf-8')
    end = datetime.now()
    delta = end - start
    print("Inventory XML qs: ", round(delta.total_seconds(), 3), "s")
    return HttpResponse(xml_string, content_type='application/xml')
```

XML apis it has same as other api that measure time lapse to measure time.

for the steps is:
- recieve all data on queryset based on models Product
- create root element for XML Structure
- then, iterate the column into each product for its products and its sub-element of product
- after iteration finished, the tostring function will convert root intu encoded UTF-8 string
- finally, it will returned as Httpresponse containing xml and content type as application/xml

### Deativate/exiting Django

for exit/quiting the server, you can use `CTRL + C` with your keyboard. The server will be terminated and back into default terminal.

### Integration Test
for the integration test, you could run by change `runserver` into `test [module]` . or in this case is
```python
python InventoryAPI/manage.py test API
```
and the output test will be printed on terminal

## Python Function

for the Python Function you could see RemoveDuplicate.py for the function.

```python
def remove_duplicate(input):
```

the remove_duplicates function will take 1 argument that name input on this function.

```python
tracking = set()
output_list = []
```

Tracking variable is set on set type to store the input iteration, while the output_list will make the output that we expected

```python
for i in input:
    if i not in tracking:
        output_list.append(i)
        tracking.add(i)
```

Then the input will iterate and if 
iteration is not in tracking variable it will add into output_list, but if on the tracking variable, it will pass into next iteration

### Unit Test

for the unit test you could run the RD_Test.py, or alternatively use this command under PythonFunction folder

```powershell
python -m unittest PythonFunction/RD_Test.py
```
