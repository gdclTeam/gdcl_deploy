from django.shortcuts import render

# Create your views here.

# 首页
def index(request):
    return render(request, 'index.html')

# 企业概况
# 企业简介
def description(request):
    return render(request, 'description.html')
# 董事长致辞
def boss(request):
    return render(request, 'boss.html')
# 组织架构
def organization(request):
    return render(request, 'organization.html')
# 公司资质
def certification(request):
    return render(request, 'certification.html')
# 公司荣誉
def reputation(request):
    return render(request, 'reputation.html')

# 企业文化
# 品牌标志
def logo(request):
    return render(request, 'logo.html')
# 管理理念
def management(request):
    return render(request, 'management.html')
# 形象展示
def show(request):
    return render(request, 'show.html')
# 企业视频
def video(request):
    return render(request, 'video.html')
# 员工风采
def employee(request):
    return render(request, 'employee.html')

# 工程业绩
# 获奖工程
def rewards(request):
    return render(request, 'rewards.html')
# 项目展示
def project_show(request):
    return render(request, 'project_show.html')
# 项目实拍
def project_photo(request):
    return render(request, 'project_photo.html')

# 新闻资讯
# 企业新闻
def company_news(request):
    return render(request, 'company_news.html')
# 行业动态
def movement(request):
    return render(request, 'movement.html')
# 通知公告
def note(request):
    return render(request, 'note.html')
# 其他资讯
def others(request):
    return render(request, 'others.html')

# 加入我们
# 人才招聘
def recruitment(request):
    return render(request, 'recruitment.html')
# 联系我们
def contact(request):
    return render(request, 'contact.html')

#银泉山庄
def yqsz(request):
    return  render(request,'yqsz.html')

#鱼林广场
def ylgc(request):
    return render(request,'ylgc.html')

#珠海港鑫和码头
def zhgxhmt(request):
    return render(request,'zhgxhmt.html')

#珠海市第九中学教学楼
def zhsdjzxjxl(request):
    return render(request,'zhsdjzxjxl.html')

#白藤湖小学
def bthxx(request):
    return render(request,'bthxx.html')


