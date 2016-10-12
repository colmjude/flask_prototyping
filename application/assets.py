# -*- coding: utf-8 -*-

import os

from flask_assets import Bundle, Environment

from lib.sass_filter import LibSass

# GOV.UK assets
css_govuk = Bundle(
  'css/govuk.scss',
  filters='scss',
  output='gen/css/govuk.css',
  depends="**/*.scss"
)

assets = Environment()

assets.register('css_govuk', css_govuk)
