from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from core.models import Commit
from .utils import date_range


# Create your views here.
@login_required
def commits(request):
    commits = Commit.objects.filter(user=request.user).order_by('created')
    now = timezone.now()
    start = now - timezone.timedelta(days=364)
    daterange = date_range(start, now)
    counts = []
    for dt in daterange:
        count = commits.filter(created__date=dt).count()
        counts.append(count)

    print(counts)

    context = {'commits': commits}
    return render(request, '', context)
