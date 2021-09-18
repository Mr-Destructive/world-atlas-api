from rest_framework import generics,status
from .models import A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z#Room 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
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

