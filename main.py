#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#




import wsgiref.handlers
from google.appengine.ext import webapp
import os
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):

  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'views/main.html')
    self.response.out.write(template.render(path, template_values))


class AssTestHandler(webapp.RequestHandler):

  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'views/test2.html')
    self.response.out.write(template.render(path, template_values))

class PubSubHandler(webapp.RequestHandler):

  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'views/pubsub.html')
    self.response.out.write(template.render(path, template_values))

class IframeHandler(webapp.RequestHandler):

  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'views/iframe.html')
    self.response.out.write(template.render(path, template_values))

class RIIframeHandler(webapp.RequestHandler):

  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'views/riiframe.html')
    self.response.out.write(template.render(path, template_values))

class TestHandler(webapp.RequestHandler):

  def get(self):
    type = self.request.get("type", "prototype")
    if type=="prototype":
      curlib = "Prototype 1.6.1"
    if type=="mootools":
      curlib = "MooTools 1.2.4"
    if type=="jquery":
      curlib = "jQuery 1.4.2 + jquery-json 2.1"
      
    template_values = {
        "type": type,
        "curlib": curlib
    }
    path = os.path.join(os.path.dirname(__file__), 'views/test.html')
    self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/test', TestHandler),
                                        ('/objtest', AssTestHandler),
                                        ('/iframe', IframeHandler),
                                        ('/pubsub', PubSubHandler),
                                        ('/riiframe', RIIframeHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
