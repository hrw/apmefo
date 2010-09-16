install:
	install -d $(DESTDIR)/opt/ApMeFo/classes/
	install -d $(DESTDIR)/opt/ApMeFo/ui
	install -d $(DESTDIR)/usr/share/doc/apmefo/
	install -d $(DESTDIR)/usr/share/applications/hildon/
	install -d $(DESTDIR)/usr/share/icons/hicolor/48x48/hildon/
	install -d $(DESTDIR)/usr/share/icons/hicolor/scalable/hildon/
	install -d $(DESTDIR)/usr/share/dbus-1/services/
	install -m 0755 src/Main.py 		$(DESTDIR)/opt/ApMeFo/
	install -m 0644 src/resources_rc.py 	$(DESTDIR)/opt/ApMeFo/
	install -m 0644 src/__init__.py 	$(DESTDIR)/opt/ApMeFo/
	install -m 0644 src/classes/*.py 	$(DESTDIR)/opt/ApMeFo/classes/
	install -m 0644 src/ui/*.py 		$(DESTDIR)/opt/ApMeFo/ui/
	install -m 0644 src/data/ApMeFo.desktop 	$(DESTDIR)/usr/share/applications/hildon/
	install -m 0644 src/data/application_apmefo_48.png 	$(DESTDIR)/usr/share/icons/hicolor/48x48/hildon/application_apmefo.png
	install -m 0644 src/data/application_apmefo_64.png 	$(DESTDIR)/usr/share/icons/hicolor/scalable/hildon/application_apmefo.png
	install -m 0644 src/data/ApMeFo.service 		$(DESTDIR)/usr/share/dbus-1/services/ApMeFo.service
