from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from .serializers import UserSerializerTest
from profiles_api import serializers, models, permissions


class ListView(APIView):
    """List proof"""
    serializer_class = serializers.ProofSerializer
    
    def get(self, request, format=None):
        """Returns a list of characteristics"""
        an_apiview = [
            'Usamos métodos HTTP como funciones (get, post, put, delete)',
            'Es similar a una vista tradicional de django', 
            'Esta mapeado a los URLs',
        ]
        
        return Response({'message': 'List', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a message with our name"""
        serializer= self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk=None):
        """Update a message with our name"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Patch_parcial modified a message with our name"""
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        """Delete a object"""
        return Response({'method': 'DELETE'})
    
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.ProofSerializer
    
    def list(self, request):
        """Returns message"""
        a_viewset = [
            'Usamos viewset para acciones (list, create, destroy, update',
            'Provee mas funcionalidad con menos codigo',
        ]
        return Response({'message': 'hola', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hola {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        """Get a object and ID"""
        return Response({'httpMethod': 'GET',})
    
    def update(self, request, pk=None):
        """Update a object"""
        return Response({'httpMethod': 'PUT',})
    
    def partial_update(self, request, pk=None):
        return Response({'httpMethod': 'PATCH',})
    
    def destroy(self, request, pk=None):
        return Response({'httpMethod': 'DELETE',})

                
class UserProfileViewSet(viewsets.ModelViewSet):
    """Create and update a user profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() ## QUERY SET.
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    
class UserLoginApiView(ObtainAuthToken):
    """Create a token for a user"""
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES
    
    
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'})

class Users(APIView):
    def get(self, request):
        queryset = models.UserProfile.objects.all()  
        dictionaries = [obj for obj in queryset.values()]
        return Response(dictionaries)

    def post(self, request):
        print(f"BODY INFO: {request.data} \n\n")
        serializer = UserSerializerTest(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        
        ## agregar línea de código, que vaya a la base de datos y me guarde
        ## lo que me mandaron en el body de la petición.
        # new_user = models.UserProfile(
        #     email=data['email'], 
        #     name=data['name'],
        #     password=data['password'])
        # new_user.save()
        return Response({"Hello": f"{data['name']}"})



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Create, read and update feed for a profile"""
    authentication_classes=(TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes= (
        permissions.UpdateOwnStatus, 
        IsAuthenticated
    )
    
    def perform_create(self, serializer):
        """Setear el perfil de usuario que esta logeado"""
        
        serializer.save(user_profile=self.request.user)
    
    


