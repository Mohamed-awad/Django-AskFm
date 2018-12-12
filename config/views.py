from django.shortcuts import render, redirect


def root(request):
  if request.user.is_authenticated:
    return redirect('/home')
  else:
    return render(request, 'askfm.html')
