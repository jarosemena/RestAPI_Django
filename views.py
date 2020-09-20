from django.vies.decorators.csrf inport csrf_exempt
from spyne.application import Application 
from sypne.decorator import rpc 
from sypne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication 
from spyne.service import ServiceBase

class SoapService(ServiceBase):
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def hello(ctx, name)
        return 'Hello, {}'.format(name)


    @rpc(Integer(nillable=False),integer(nillable=False), _returns=integer)
    def sum(ctx, a, b):
        return int(a+b)


soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)   


django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)