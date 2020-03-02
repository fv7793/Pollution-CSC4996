from mongoengine import connect
from peat import Peat

db = connect(db="Pollution")
db.drop_database("Pollution")

peat = Peat(["pollution"])

articles = peat.getScrapedArticles()
print("\n\n")
print(articles[0]['url'])
print(articles[0]['title'])
print(articles[0]['publishingDate'])
# peat.storeInArticlesCollection(articles[0])















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
