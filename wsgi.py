#Heroku's tutorial created its django project in the git root, so we
#have to hack in the path for our separate project folder and wsgi.
import sys
sys.path.append('project')

from project.wsgi import application
from dj_static import Cling

application = Cling(application)
