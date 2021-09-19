from rest_framework import generics,status
from .models import A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
import random

# Create your views here.

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

