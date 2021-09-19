from rest_framework import generics,status
from .models import A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
import random

from .serializers import (
        PlaceASerializer, PlaceBSerializer, PlaceCSerializer, PlaceDSerializer, PlaceESerializer,
        PlaceFSerializer, PlaceGSerializer, PlaceHSerializer, PlaceISerializer, PlaceJSerializer,
        PlaceKSerializer, PlaceLSerializer, PlaceMSerializer, PlaceNSerializer, PlaceOSerializer,
        PlacePSerializer, PlaceQSerializer, PlaceRSerializer, PlaceSSerializer, PlaceTSerializer,
        PlaceUSerializer, PlaceVSerializer, PlaceWSerializer, PlaceXSerializer, PlaceYSerializer,
        PlaceZSerializer)

# Create your views here.
class addPlace(APIView):
    def get(self, request, place):
        place = place.lower()
        if(place[0]=='a'):
            data = {'a': place }
            serializer = PlaceASerializer(data=data)
        if(place[0]=='b'):
            data = {'b': place }
            serializer = PlaceBSerializer(data=data)
        if(place[0]=='c'):
            data = {'c': place }
            serializer = PlaceCSerializer(data=data)
        if(place[0]=='d'):
            data = {'d': place }
            serializer = PlaceDSerializer(data=data)
        if(place[0]=='e'):
            data = {'e': place }
            serializer = PlaceESerializer(data=data)
        if(place[0]=='f'):
            data = {'f': place }
            serializer = PlaceFSerializer(data=data)
        if(place[0]=='g'):
            data = {'g': place }
            serializer = PlaceGSerializer(data=data)
        if(place[0]=='h'):
            data = {'h': place }
            serializer = PlaceHSerializer(data=data)
        if(place[0]=='i'):
            data = {'i': place }
            serializer = PlaceISerializer(data=data)
        if(place[0]=='j'):
            data = {'j': place }
            serializer = PlaceJSerializer(data=data)
        if(place[0]=='k'):
            data = {'k': place }
            serializer = PlaceKSerializer(data=data)
        if(place[0]=='l'):
            data = {'l': place }
            serializer = PlaceLSerializer(data=data)
        if(place[0]=='m'):
            data = {'m': place }
            serializer = PlaceMSerializer(data=data)
        if(place[0]=='n'):
            data = {'n': place }
            serializer = PlaceNSerializer(data=data)
        if(place[0]=='o'):
            data = {'o': place }
            serializer = PlaceOSerializer(data=data)
        if(place[0]=='p'):
            data = {'p': place }
            serializer = PlacePSerializer(data=data)
        if(place[0]=='q'):
            data = {'q': place }
            serializer = PlaceQSerializer(data=data)
        if(place[0]=='r'):
            data = {'r': place }
            serializer = PlaceRSerializer(data=data)
        if(place[0]=='s'):
            data = {'s': place }
            serializer = PlaceSSerializer(data=data)
        if(place[0]=='t'):
            data = {'t': place }
            serializer = PlaceTSerializer(data=data)
        if(place[0]=='u'):
            data = {'u': place }
            serializer = PlaceUSerializer(data=data)
        if(place[0]=='v'):
            data = {'v': place }
            serializer = PlaceVSerializer(data=data)
        if(place[0]=='w'):
            data = {'w': place }
            serializer = PlaceWSerializer(data=data)
        if(place[0]=='x'):
            data = {'x': place }
            serializer = PlaceXSerializer(data=data)
        if(place[0]=='y'):
            data = {'y': place }
            serializer = PlaceYSerializer(data=data)
        if(place[0]=='z'):
            data = {'z': place }
            serializer = PlaceZSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getPlace(APIView):
    def get(self, request, letter):
        if letter == 'a':
            place = list(A.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['a']})

        if letter == 'b':
            place = list(B.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['b']})

        if letter == 'c':
            place = list(C.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['c']})

        if letter == 'd':
            place = list(D.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['d']})

        if letter == 'e':
            place = list(E.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['e']})

        if letter == 'f':
            place = list(F.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['f']})

        if letter == 'g':
            place = list(G.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['g']})

        if letter == 'h':
            place = list(H.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['h']})

        if letter == 'i':
            place = list(I.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['i']})

        if letter == 'j':
            place = list(J.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['j']})

        if letter == 'k':
            place = list(K.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['k']})

        if letter == 'l':
            place = list(L.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['l']})

        if letter == 'm':
            place = list(M.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['m']})

        if letter == 'n':
            place = list(N.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['n']})

        if letter == 'o':
            place = list(O.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['o']})

        if letter == 'p':
            place = list(P.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['p']})

        if letter == 'q':
            place = list(Q.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['q']})

        if letter == 'r':
            place = list(R.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['r']})

        if letter == 's':
            place = list(S.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['s']})

        if letter == 't':
            place = list(T.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['t']})

        if letter == 'u':
            place = list(U.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['u']})

        if letter == 'v':
            place = list(V.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['v']})

        if letter == 'w':
            place = list(W.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['w']})

        if letter == 'x':
            place = list(X.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['x']})

        if letter == 'y':
            place = list(Y.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['y']})

        if letter == 'z':
            place = list(Z.objects.values())
            place = random.choice(place)
            return JsonResponse({letter:place['z']})


class ifPlace(APIView):
    def get(self, request, place):
        if place[0] == 'a':
            if A.objects.filter(a=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'b':
            if B.objects.filter(b=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'c':
            if C.objects.filter(c=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'd':
            if D.objects.filter(d=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'e':
            if E.objects.filter(e=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'f':
            if F.objects.filter(f=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'g':
            if G.objects.filter(g=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'h':
            if H.objects.filter(h=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'i':
            if I.objects.filter(i=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'j':
            if J.objects.filter(j=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'k':
            if K.objects.filter(k=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'l':
            if L.objects.filter(l=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'm':
            if M.objects.filter(m=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'n':
            if N.objects.filter(n=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'o':
            if O.objects.filter(o=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'p':
            if P.objects.filter(p=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'q':
            if Q.objects.filter(q=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 'r':
            if R.objects.filter(s=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

        if place[0] == 's':
            if S.objects.filter(s=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 't':
            if T.objects.filter(t=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'u':
            if U.objects.filter(u=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'v':
            if V.objects.filter(k=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'w':
            if W.objects.filter(w=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'x':
            if X.objects.filter(x=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'y':
            if Y.objects.filter(y=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})


        if place[0] == 'z':
            if Z.objects.filter(z=place).exists():
                return JsonResponse({'result':True})
            else:
                return JsonResponse({'result':False})

class getList(APIView):
    def get(self, request, letter):

        if letter == 'a':
            place = list(A.objects.values_list('a',flat=True))
            return JsonResponse({letter:place})

        if letter == 'b':
            place = list(B.objects.values_list('b',flat=True))
            return JsonResponse({letter:place})

        if letter == 'c':
            place = list(C.objects.values_list('c',flat=True))
            return JsonResponse({letter:place})

        if letter == 'd':
            place = list(D.objects.values_list('d',flat=True))
            return JsonResponse({letter:place})

        if letter == 'e':
            place = list(E.objects.values_list('e',flat=True))
            return JsonResponse({letter:place})

        if letter == 'f':
            place = list(f.objects.values_list('f',flat=True))
            return JsonResponse({letter:place})

        if letter == 'g':
            place = list(G.objects.values_list('g',flat=True))
            return JsonResponse({letter:place})

        if letter == 'h':
            place = list(H.objects.values_list('h',flat=True))
            return JsonResponse({letter:place})

        if letter == 'i':
            place = list(I.objects.values_list('i',flat=True))
            return JsonResponse({letter:place})

        if letter == 'j':
            place = list(J.objects.values_list('j',flat=True))
            return JsonResponse({letter:place})

        if letter == 'k':
            place = list(K.objects.values_list('k',flat=True))
            return JsonResponse({letter:place})

        if letter == 'l':
            place = list(L.objects.values_list('l',flat=True))
            return JsonResponse({letter:place})

        if letter == 'm':
            place = list(M.objects.values_list('m',flat=True))
            return JsonResponse({letter:place})

        if letter == 'n':
            place = list(N.objects.values_list('n',flat=True))
            return JsonResponse({letter:place})

        if letter == 'o':
            place = list(O.objects.values_list('o',flat=True))
            return JsonResponse({letter:place})

        if letter == 'p':
            place = list(P.objects.values_list('p',flat=True))
            return JsonResponse({letter:place})

        if letter == 'q':
            place = list(Q.objects.values_list('q',flat=True))
            return JsonResponse({letter:place})

        if letter == 'r':
            place = list(R.objects.values_list('r',flat=True))
            return JsonResponse({letter:place})

        if letter == 's':
            place = list(S.objects.values_list('s',flat=True))
            return JsonResponse({letter:place})

        if letter == 't':
            place = list(T.objects.values_list('t',flat=True))
            return JsonResponse({letter:place})

        if letter == 'u':
            place = list(U.objects.values_list('u',flat=True))
            return JsonResponse({letter:place})

        if letter == 'v':
            place = list(V.objects.values_list('v',flat=True))
            return JsonResponse({letter:place})

        if letter == 'w':
            place = list(W.objects.values_list('w',flat=True))
            return JsonResponse({letter:place})

        if letter == 'x':
            place = list(X.objects.values_list('x',flat=True))
            return JsonResponse({letter:place})

        if letter == 'y':
            place = list(Y.objects.values_list('y',flat=True))
            return JsonResponse({letter:place})

        if letter == 'z':
            place = list(Z.objects.values_list('z',flat=True))
            return JsonResponse({letter:place})
