from Subscrap.models import *
from Subscrap.forms import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar


def gettheduedate(startdate, renewal ):
    n = 0
    start = startdate
    date_time = start.strftime("%y/%m/%d")

    date_format = '%y/%m/%d'
    dtObj = datetime.strptime(date_time, date_format)
    
    n = renewal
    future_date = dtObj + relativedelta(months=n)
    #test = dtObj - relativedelta(months=n)
    return future_date
    

def gettotalcost():
    current_year = datetime.now().year
    current_month = datetime.now().month
    validitems = sublist.objects.filter(startDate__month__gte= current_month, startDate__year__gte= current_year, is_active = True )
    total_price = sum(validitems.values_list('cost', flat=True))
    return total_price

def month_name(month_number):
   return calendar.month_name[month_number]


def make_sub():
    musician = prebuildsublist.objects.create(
                name="Spotify", image='images/Spotify.png', website="https://www.spotify.com/", subtype='Music'
        )
        
    musician = prebuildsublist.objects.create(
                name="Hulu", image='images/Hulu.png', website="https://www.hulu.com/", subtype='Video'
        )
        
    musician = prebuildsublist.objects.create(
                name="Dollar Shave Club", image='images/razor.png', website="https://www.dollarshaveclub.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="HelloFresh", image='images/hellofresh.png', website="https://www.hellofresh.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Disney+", image='images/disneyplus.jpg', website="https://www.disneyplus.com/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="HomeChef", image='images/chef.png', website="https://www.homechef.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Twitch", image='images/twitch.png', website="https://www.twitch.tv/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="CrunchyRoll", image='images/crunchyroll.png', website="https://www.crunchyroll.com/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="Amazon Prime", image='images/prime.png', website="https://www.amazon.com/amazonprime/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="Youtube Premium", image='images/youtube.png', website="https://www.youtube.com/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="Audible", image='images/audbile.png', website="https://www.audible.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Playstation Plus", image='images/playstation.png', website="https://www.playstation.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Xbox Game Pass", image='images/xbox.png', website="https://www.xbox.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Xbox Live", image='images/xbox.png', website="https://www.xbox.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Wall Street Journal", image='images/news.png', website="https://www.wsj.com/", subtype='News'
        )
    musician = prebuildsublist.objects.create(
                name="Grub Hub", image='images/chef.png', website="https://www.grubhub.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Nintendo Online", image='images/nintendo.png', website="https://www.nintendo.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Discord Nitro", image='images/discord.png', website="https://www.discord.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Google Stadia", image='images/stadia.png', website="https://www.stadia.google.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Bokksu", image='images/chef.png', website="https://www.bokksu.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Origin Access", image='images/origin.png', website="https://www.origin.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Blue Apron", image='images/chef.png', website="https://www.blueapron.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="World Of Warcraft", image='images/wow.png', website="https://www.worldofwarcraft.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="GForceNow", image='images/computer.png', website="https://www.nvidia.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="MasterClass", image='images/class.png', website="https://www.masterclass.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Brillant", image='images/class.png', website="https://www.brillant.org/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Annie's Creative Studio", image='images/class.png', website="https://www.anniecatalog.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Man Scaped", image='images/razor.png', website="https://www.manscaped.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Philo", image='images/tv.png', website="https://www.philo.com/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="Scribd", image='images/scribd.png', website="https://www.scribd.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Apple News+", image='images/news.png', website="https://www.apple.com/", subtype='News'
        )
    musician = prebuildsublist.objects.create(
                name="Blinkist", image='images/class.png', website="https://www.blinkist.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Wondrium", image='images/class.png', website="https://www.wondrium.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Kindle Unlimited", image='images/ebook.png', website="https://www.amazon.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Epic! Books", image='images/ebook.png', website="https://www.getepic.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Amazon Music Unlimited", image='images/prime.png', website="https://www.amazon.com/", subtype='Music'
        )
    musician = prebuildsublist.objects.create(
                name="Goddess Provisions Moon Wisdom", image='images/makeup.png', website="https://www.digital.goddessprovisions.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Noom", image='images/chef.png', website="https://www.noom.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Hertz My Car", image='images/car.png', website="https://www.hertz.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Vooks", image='images/class.png', website="https://www.vooks.com/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="Babbel", image='images/class.png', website="https://www.babbel.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Birchbox", image='images/makeup.png', website="https://www.birchbox.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Glossybox", image='images/makeup.png', website="https://www.glossbox.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Ipsy", image='images/makeup.png', website="https://www.ipsy.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Julep Maven", image='images/makeup.png', website="https://www.julep.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Sephora Play!", image='images/makeup.png', website="https://www.sephora.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="FabFitFun", image='images/makeup.png', website="https://www.fabfitfun.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Beauty Box 5", image='images/makeup.png', website="https://www.findsubscriptionboxes.com/box/beauty-box-5/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Laurel & Reed", image='images/makeup.png', website="https://www.laurelandreed.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Love Goodly", image='images/makeup.png', website="https://www.lovegoodly.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Merkaela", image='images/makeup.png', website="https://www.merkaela.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Terra Bella Box", image='images/makeup.png', website="https://www.terrabellabox.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Target Beauty Box", image='images/makeup.png', website="https://www.target.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Birchbox Man", image='images/razor.png', website="https://www.birchbox.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Sock Panda", image='images/suit.png', website="https://www.sockpanda.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Trunk Club", image='images/suit.png', website="https://www.trunkclub.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Five Four Club", image='images/sock.png', website="https://www.fivefourclub.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Watch Gang", image='images/suit.png', website="https://www.watchgang.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Bookishly Book Club", image='images/ebook.png', website="https://www.bookishly.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Loot Crate", image='images/games.png', website="https://www.lootcrate.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Nerd Block", image='images/games.png', website="https://www.nerdblock.com/", subtype='Video'
        )
    musician = prebuildsublist.objects.create(
                name="Geek Fuel", image='images/games.png', website="https://www.geekfuel.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Kal-Elle Fandom Monthly", image='images/suit.png', website="https://www.kalellefandommonthly.cratejoy.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Charm With Me Club", image='images/suit.png', website="https://www.charmwithmeclub.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Accio!", image='images/suit.png', website="https://www.acciobox.cratejoy.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Geek Gear", image='images/suit.png', website="https://www.geekgearbox.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Escape the Crate", image='images/games.png', website="https://www.escape-the-crate.com/", subtype='Access'
        )
    musician = prebuildsublist.objects.create(
                name="Kiwi Crate", image='images/class.png', website="https://www.kiwico.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Honesty Company", image='images/makeup.png', website="https://www.honest.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Bookroo", image='images/ebook.png', website="https://www.bookroo.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Love With Food", image='images/chef.png', website="https://www.lovewithfood.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Japan Crate", image='images/chef.png', website="https://www.japancrate.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Atlas Coffee Club", image='images/coffee.png', website="https://www.atlascoffeeclub.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Tea Runners", image='images/coffee.png', website="https://www.tearunners.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Carnivore Club Co", image='images/chef.png', website="https://www.carnivoreclub.co/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Cocoa Runners", image='images/coffee.png', website="https://www.cocoarunners.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Jerky Snob", image='images/chef.png', website="https://www.jerkysnob.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Shaker & Spoon", image='images/chef.png', website="https://www.shakerandspoon.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Turntable Kitchen", image='images/chef.png', website="https://www.turntablekitchen.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Beer of the Month", image='images/alcohol.png', website="https://www.beermonthclub.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Craft Coffee", image='images/coffee.png', website="https://www.craftcoffee.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="SaloonBox DIY Cocktail Club", image='images/alcohol.png', website="https://www.saloonbox.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="The Mantry", image='images/chef.png', website="https://www.mantry.com/", subtype='Lifestyle'
        )
    musician = prebuildsublist.objects.create(
                name="Raw Spice Bar", image='images/chef.png', website="https://www.rawspicebar.com/", subtype='Lifestyle'
        )