from django.http import JsonResponse
from TestModel.models import UserInfo, CrawlerTask
from django.utils import timezone


def create_task(request):
    user = request.session.get('user_name')
    req_state = {}
    try:
        info = UserInfo.objects.get(user_name=user)
        if info.task_state:
            print('已有任务')
            req_state['state'] = 0
            return JsonResponse(req_state)
        else:
            info.task_state = True
            info.save()
            platform = "weChat"
            account = request.POST.get('account')
            weChatID = request.POST.get('weChatID')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            task_start = timezone.now()
            CrawlerTask.objects.create(user_name=user, platform=platform, account=account, weChatID=weChatID, crawl_start=start_date, crawl_end=end_date, task_start=task_start, task_end=task_start)
            print('success')
            req_state['state'] = 1

    except KeyError:
        req_state['state'] = 2

    return JsonResponse(req_state)