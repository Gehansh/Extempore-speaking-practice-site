import random
from django.http import HttpResponse
from django.shortcuts import render
from ext_app.models import meetinfo


def index(request):
    return render(request,'index.html')

def link(request):
    topiclist=["Indian flag","Covid 19 effect on people","Anime should be banned?","Everyone should have hobby!","A college degree is essential for getting a good job" , "Are student loans exploitative" , "All students should have to purchase a laptop" , "Boarding school is harmful to students" , "Cell phones should be banned in schools" , "College should be free for everyone" , "Contact sports should be required in school" , "Education should be privatized" , "Education should focus on maths and science rather than music and art" , "Fast food should be banned in schools" , "Homeschooling is better than traditional schooling" , "Public schools are better than private schools" , "Religion should be taught in schools" , "Should free STD testing be offered in schools" , "Schools should have armed guards" , "Should standardized testing be abolished" , "School uniforms should be mandatory" , "Student loans should be forgiven" , "Studying a second language should be compulsory" , "Teachers should be given guns to defend students" , "Teachers should be paid as much as doctors" , "All people should be able to own guns" , "All prisons should be governmentally owned and run" , "Britain should leave the European Union" , "Churches should pay taxes" , "Communism is not a good political ideology" , "Is freedom of speech a necessity in a functional society" , "Is owning an automatic weapon morally justifiable" , "Is patriotism ultimately destructive to international relations" , "Is the US voting system democratic" , "Juries should include 24 jurors instead of 12" , "Politics should be kept out of schools" , "Presidential terms should be limited to two years instead of four" , "Rich people and large corporations should pay more taxes" , "Should illegal immigrants be treated as criminals" , "Should the U.N. have a standing army" , "Should the voting age be lowered to 16" , "Should there be limits on the First Amendment (free speech)" , "Should your country make a land claim on Antarctica" , "The British Monarchy should be abolished" , "The country should allow more refugees to enter" , "The U.S. should intervene in overseas conflicts" , "The US should abolish the electoral college" , "The West should lift all sanctions on Iran (or North Korea)" , "Vaccination should be mandatory" , "Voting should be mandatory for all citizens" , "Abortion should be available to all women" , "Barbie is a good role model for young girls" , "Burning the flag should be illegal" , "Can censorship ever be justified" , "Censorship is sometimes warranted on the internet" , "Cigarettes should be banned" , "Companies should be required to hire 50% male and 50% female employees" , "Drug addicts should be helped rather than punished" , "Drug use should be treated as a mental health issue rather than a criminal offense" , "Euthanasia should be legal" , "Feminism should focus more on men's rights" , "Has the #MeToo movement gone too far" , "Healthcare should be universal" , "Is feminism irrelevant in the 21st century" , "Is graffiti art just as worthy of regard as classical paintings" , "Is privacy important" , "Peer pressure is a good thing" , "Police should be allowed to use deadly force" , "Religion does more harm than good" , "Should genetic engineering be legal" , "Should human cloning be legalized" , "Should insurance cover cosmetic procedures" , "Smoking should be banned" , "Social media does more harm than good" , "The death penalty should be abolished" , "The government should provide free birth control" , "The harms of patriotism outweigh the benefits" , "The minimum wage should be lowered (or raised)" , "We're living in a dystopian society"]
    callurl="https://meet.jit.si/Extempore-debate-99zAyy33w1pPQ"
    obj=meetinfo.objects.get(perma=1)
    tag=int(obj.idtag)
    topicno=int(obj.topicno)
    obj.idtag=tag+1
    if(tag%2==0):
        callurl=callurl+str(tag+1)
        n=random.randint(0,len(topiclist)-1)
        obj.topicno=n
        topic_name=topiclist[n]
    else:
        callurl=callurl+str(tag)
        n=topicno
    topic_name=topiclist[n]
    obj.save()
    param={'callurl':callurl,'topic':topic_name}
    return render(request,'link.html',param)

