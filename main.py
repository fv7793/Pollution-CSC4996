from websites import *
import newspaper
import requests
from bs4 import BeautifulSoup as soup

keywords = ["pollution"]

ourmidland = Ourmidland(keywords)
marionPress = MarionPress(keywords)
theCountyPress = TheCountyPress(keywords)
lakeCountyStar = LakeCountyStar(keywords)
northernExpress = NorthernExpress(keywords)
manisteeNews = ManisteeNews(keywords)
michiganChronicle = MichiganChronicle(keywords)
clarkstonNews = ClarkstonNews(keywords)
harborLightNews = HarborLightNews(keywords)
theDailyNews = TheDailyNews(keywords)
lakeOrionReview = LakeOrionReview(keywords)
leelanauNews = LeelanauNews(keywords)
houghtonLakeResorter = HoughtonLakeResorter(keywords)
ironMountainDailyNews = IronMountainDailyNews(keywords)
miningJournal = MiningJournal(keywords)
theAlpenaNews = TheAlpenaNews(keywords)

websites = [ourmidland,marionPress,theCountyPress,lakeCountyStar,northernExpress,manisteeNews,michiganChronicle,
            clarkstonNews,harborLightNews,theDailyNews,lakeOrionReview,leelanauNews,houghtonLakeResorter,
            ironMountainDailyNews,miningJournal,theAlpenaNews]

for website in websites:
    print("\n\n" + website.baseUrl)
    for article in website.getArticleLinks():
        print(article)







# urls = \
#     ["https://www.ourmidland.com/news/article/Fifth-annual-Great-Lakes-Mom-Prom-raises-over-15094533.php",
# "https://www.ourmidland.com/news/article/Midland-schools-combat-teen-vaping-15094503.php",
# "https://www.ourmidland.com/news/article/Vascular-center-meets-fundraising-goal-15094499.php",
# "https://www.ourmidland.com/news/article/Shelterhouse-to-begin-move-in-new-15094501.php",
# "https://www.ourmidland.com/sports/article/Emotional-roller-coaster-NU-women-beat-SVSU-15091484.php",
# "https://www.ourmidland.com/sports/article/Magical-night-NU-men-beat-SVSU-earn-1st-ever-15091394.php",
# "https://www.ourmidland.com/sports/article/Fab-freshman-Molly-Davis-playing-big-role-in-15087874.php",
# "https://www.ourmidland.com/sports/article/NU-s-Colestock-reaches-milestone-announces-15081314.php",
# "https://www.ourmidland.com/lifestyles/article/Throwback-Midland-City-Police-part-2-12842043.php",
# "https://www.ourmidland.com/lifestyles/article/Things-to-Do-Feb-29-and-beyond-15094526.php",
# "https://www.ourmidland.com/lifestyles/article/Creative-360-luncheon-celebrates-Marilyn-Clark-15091476.php",
# "https://www.ourmidland.com/lifestyles/article/Things-to-Do-Feb-28-and-beyond-15091463.php"]
#
# for url in urls:
#     # article = newspaper.Article(url)
#     # article.download()
#     # article.parse()
#     # print(article.title)
#
#     page = requests.get(url)
#     soupPage = soup(page.content, 'html.parser')
#     print(soupPage.find("title"))
