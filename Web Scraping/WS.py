import bs4 , requests

def getAmazonprice(productUrl):
   res = requests.get(productUrl)
   res.raise_for_status() 
   soup = bs4.BeautifulSoup(res.text, 'html.parser')
   elems = soup.select('html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember.nav-ewc-persistent-hover.nav-ewc-compact-view.nav-ewc-wider-compact-view body.a-aui_72554-c.a-aui_accordion_a11y_role_354025-t1.a-aui_killswitch_csa_logger_372963-c.a-aui_pci_risk_banner_210084-c.a-aui_preload_261698-c.a-aui_rel_noreferrer_noopener_309527-c.a-aui_template_weblab_cache_333406-c.a-aui_tnr_v2_180836-c.a-meter-animate div#a-page div#dp.book.en_IN div#dp-container.a-container div.celwidget div#centerCol.centerColumn div#MediaMatrix.celwidget div#formats.a-section.a-spacing-large.responsive div#tmmSwatches.a-row ul.a-unordered-list.a-nostyle.a-button-list.a-horizontal li.swatchElement.selected.resizedSwatchElement span.a-list-item span#a-autoid-2.a-button.a-button-selected.a-spacing-mini.a-button-toggle.format span.a-button-inner a#a-autoid-2-announce.a-button-text span.a-color-base span.a-size-base.a-color-price')
   return elems[0].text.strip()



price = getAmazonprice('https://www.amazon.in/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?keywords=automate+the+boring+stuff+with+python+3rd+edition&qid=1689690192&s=books&sprefix=Automate+the%2Cstripbooks%2C205&sr=1-1')  
print('This is the price of the book' + price)