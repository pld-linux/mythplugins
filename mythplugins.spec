#
# Conditional build:
%bcond_without	binary		# skip building binary plugins (build only mythweb)
%bcond_without	mytharchive	# disable building mytharchive plugin
%bcond_without	mythbrowser	# disable building building mythbrowser plugin
%bcond_without	mythnetvision	# disable building mythnetvision plugin
%bcond_without	mythgallery	# disable building mythgallery plugin
%bcond_without	mythgame	# disable building mythgame plugin
%bcond_without	mythmusic	# disable building mythmusic plugin
%bcond_without	mythnews	# disable building mythnews plugin
# Mythweather disabled, as we need DateTime::Format::ISO8601 first
# not present by default in PLD
%bcond_with	mythweather	# enable building mythweather plugin
%bcond_without	mythweb		# disable building mythweb plugin
%bcond_without  mythzoneminder  # disable building mythzoneminder plugin

%if %{without binary}
%undefine	with_mytharchive
%undefine	with_mythbrowser
%undefine	with_mythnetvision
%undefine	with_mythgallery
%undefine	with_mythgame
%undefine	with_mythmusic
%undefine	with_mythnews
%undefine	with_mythweather
%endif


Summary:	Main MythTV plugins
Summary(pl.UTF-8):	Główne wtyczki MythTV
Name:		mythplugins
Version:	0.26.1
Release:	12
License:	GPL v2
Group:		Applications/Multimedia
Source0:	ftp://ftp.osuosl.org/pub/mythtv/%{name}-%{version}.tar.bz2
# Source0-md5:	d896d9f9313ba5dd95e2e977bf9c0f8f
Source1:	mythweb-apache.conf
Source2:	mythweb_lighttpd.conf
Source3:	htdigest.sh
Source4:	http_servers_conf_tips.txt
Source5:	mythweb-httpd.conf
Patch0:		mythweb-chdir.patch
Patch1:		system-zmq.patch
Patch2:		cxx11.patch
Patch3:		gcc11.patch
Patch10:	%{name}-compile_fixes_for_qt_4_7.patch
Patch20:	%{name}-mytharchive-INT64.patch
URL:		http://www.mythtv.org/
%if %{with binary}
%if %{with mythgallery} || %{with mythmusic}
BuildRequires:	OpenGL-devel
%endif
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	SDL-devel
BuildRequires:	a52dec-libs-devel
BuildRequires:	faad2-devel >= 2.0-5.2
%if %{with mythmusic}
BuildRequires:	cdparanoia-III-devel
BuildRequires:	fftw3-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	flac-devel >= 1.0.4
BuildRequires:	lame-libs-devel
BuildRequires:	libcdaudio-devel >= 0.99.12p2
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	taglib-devel
%endif
BuildRequires:	freetype-devel
BuildRequires:	libdvdcss-devel >= 1.2.7
BuildRequires:	libdvdread-devel >= 0.9.4
%{?with_mythgallery:BuildRequires:	libexif-devel >= 1:0.6.9}
BuildRequires:	libfame-devel >= 0.9.0
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmyth-devel > 0.26
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libvisual-devel
BuildRequires:	mjpegtools-devel >= 1.6.1
BuildRequires:	nasm
BuildRequires:	patchutils
%{?with_mythweather:BuildRequires:      perl-DateTime-Format-ISO8601}
%{?with_mythweather:BuildRequires:      perl-Image-Size}
%{?with_mythweather:BuildRequires:	perl-XML-Simple}
%{?with_mythweather:BuildRequires:      perl-XML-XPath}
%if %{with mythnetvision}
BuildRequires:	python-MythTV
BuildRequires:	python-lxml
BuildRequires:	python-oauth
%endif
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
%{?with_mythmusic:BuildRequires:        taglib-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xvid-devel >= 1:0.9.1
BuildRequires:	zlib-devel
%endif
%{?with_mytharchive:Requires:	mytharchive}
%{?with_mythbrowser:Requires:	mythbrowser}
%{?with_mythgallery:Requires:	mythgallery}
%{?with_mythgame:Requires:	mythgame}
%{?with_mythmysic:Requires:	mythmusic}
%{?with_mythnetvision:Requires:	mythnetvision}
%{?with_mythnews:Requires:	mythnews}
%{?with_mythweather:Requires:	mythweather}
%{?with_mythweb:Requires:	mythweb}
Obsoletes:	mythdvd < %{version}-%{release}
Obsoletes:	mythmovies < %{version}-%{release}
Obsoletes:	mythvideo
ExclusiveArch:	%{ix86} %{x8664} x32 ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		myth_api_version %(awk -vFS=. '/^LIBVERSION/{sub("LIBVERSION = ", ""); printf ("%s.%s", $1, $2)}' %{_datadir}/mythtv/build/settings.pro 2>/dev/null || echo ERROR)
%define		_webapps	/etc/webapps
%define		_webapp		mythweb

%description
This is a consolidation of all the official MythTV plugins that used
to be distributed as separate downloads from mythtv.org.

%description -l pl.UTF-8
Jest to zbiór wszystkich oficjalnych wtyczek MythTV, które były
wcześniej rozpowszechniane jako osobne pakiety na mythtv.org.

%package -n mytharchive
Summary:	A MythTV module to create and burn DVDs
Summary(pl.UTF-8):	Moduł MythTV do tworzenia i wypalania DVD
Group:		Applications/Multimedia
Requires:	dvdauthor
Requires:	mjpegtools
Requires:	mythtv-frontend-api = %{myth_api_version}
Requires:	python-MySQLdb
Requires:	python-PIL
Suggests:	dvdrtools-mkisofs

%description -n mytharchive
MythArchive is a MythTV style plugin that uses the Mythburn Script to
create and burn DVDs from MythTV recordings, MythVideo files or any
video files available on a MythTV system. It can also export
recordings to a native archive format that can then be imported back
into a MythTV system restoring all the associated metadata.

%description -n mytharchive -l pl.UTF-8
MythArchive to wtyczka MythTV używająca skryptu Mythburn do tworzenia
i wypalania płyt DVD z nagrań MythTV, plików MythVideo lub dowolnych
innych plików z filmami dostępnych w systemie MythTV. Może także
eksportować nagrania do natywnego formatu archiwum, który potem można
zaimportować z powrotem do systemu MythTV przywracając wszystkie
związane z nimi metadane.

%package -n mythmusic
Summary:	The music player add-on module for MythTV
Summary(pl.UTF-8):	Moduł odtwarzacza muzyki dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythmusic
Music add-on for MythTV. Support playlists, visualisations, tag
editing and plays many popular audio file formats - mp3, flac, wav,
ogg etc.

%description -n mythmusic -l pl.UTF-8
Odtwarzacz muzyki dla MythTV. Obsługuje listy odtwarzania,
wizualizacje, edycję tagów. Potrafi odtwarzać wiele popularnych
formatów audio - mp3, flac, wav, ogg itd.

%package -n mythweather
Summary:	A MythTV module that displays a weather forcast
Summary(pl.UTF-8):	Moduł MythTV wyświetlający prognozę pogody
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythweather
A MythTV module that displays a weather forcast.

%description -n mythweather -l pl.UTF-8
Moduł MythTV wyświetlający prognozę pogody.

%package -n mythgallery
Summary:	A gallery/slideshow module for MythTV
Summary(pl.UTF-8):	Moduł galerii/pokazu slajdów dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythgallery
A gallery/slideshow module for MythTV.

%description -n mythgallery -l pl.UTF-8
Moduł galerii/pokazu slajdów dla MythTV.

%package -n mythgame
Summary:	A game frontend (xmame, nes, snes, pc) for MythTV
Summary(pl.UTF-8):	Interfejs do gier (xmame, nes, snes, pc) dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythgame
A game frontend (xmame, nes, snes, pc) for MythTV.

%description -n mythgame -l pl.UTF-8
Interfejs do gier (xmame, nes, snes, pc) dla MythTV.

%package -n mythnews
Summary:	A RSS News Feed plugin for MythTV
Summary(pl.UTF-8):	Wtyczka czytnika nowinek RSS dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythnews
A RSS News Feed plugin for MythTV.

%description -n mythnews -l pl.UTF-8
Wtyczka czytnika nowinek RSS dla MythTV.

%package -n mythbrowser
Summary:	A small web browser module for MythTV
Summary(pl.UTF-8):	Moduł małej przeglądarki WWW dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythbrowser
MythBrowser is a full fledged web-browser (multiple tabs) to display
webpages in full-screen mode. Simple page navigation is possible.
Starting with version 0.13 it also has full support for mouse driven
navigation (right mouse opens and closes the popup menu).

MythBrowser also contains a BookmarkManager to manage the website
links in a simple mythplugin.

%description -n mythbrowser -l pl.UTF-8
MythBrowser to w pełni funkcjonalna przeglądarka WWW (z wieloma
zakładkami) wyświetlająca strony WWW w trybie pełnoekranowym. Możliwa
jest prosta nawigacja po stronie. Począwszy od wersji 0.13 ma pełną
obsługę nawigacji myszką (prawy przycisk otwiera i zamywa wyskakujące
menu).

MythBrowser zawiera także BookmarkManagera do zarządzania odnośnikami
do stron w prostej wtyczce myth.

%package -n mythweb
Summary:	The web interface to MythTV
Summary(pl.UTF-8):	Interfejs WWW do MythTV
Group:		Applications/Multimedia
Requires:	php(mysql)
Requires:	php(posix)
Requires:	webapps
Requires:	webserver(php) >= 4.3
Conflicts:	apache-base < 2.4.0-1

%description -n mythweb
The web interface to MythTV.

%description -n mythweb -l pl.UTF-8
Interfejs WWW do MythTV.

%package -n mythnetvision
Summary:	Mythtv extension to watch network movie shows
Summary(pl.UTF-8):	Dodatek do MythTV do oglądania sieciowych transmisji
Group:		Applications/Multimedia
Requires:	mythbrowser
Requires:	mythtv-frontend-api = %{myth_api_version}
Requires:	python-MythTV
Requires:	python-oauth

%description -n mythnetvision
Mythtv extension to watch network movie shows (ex. YouTube).

%description -n mythnetvision -l pl.UTF-8
Dodatek do MythTV do oglądania sieciowych transmisji. Na przykład z
YouTube.

%package -n mythzoneminder
Summary:	MythTV security TV manager
Summary(pl.UTF-8):	Obsługa kamer przemysłowych dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythzoneminder
MythTV security TV manager.

%description -n mythzoneminder -l pl.UTF-8
Obsługa kamer przemysłowych dla MythTV.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
#%%patch -P10 -p1
%patch -P20 -p1

# lib64 fix - enable to update patch
%if "%{_lib}" != "lib" && 0
find '(' -name '*.[ch]' -o -name '*.cpp' -o -name '*.pro' ')' | \
xargs grep -l /lib/ . | xargs sed -i -e '
s,%{_prefix}/lib/,/%{_lib}/,g
	s,{PREFIX}/lib,{PREFIX}/%{_lib},g
'
exit 1
%endif

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' \
      mytharchive/mythburn/scripts/mythburn.py \
      mythgame/mythgame/scripts/giantbomb.py \
      mythgame/mythgame/scripts/giantbomb/giantbomb_api.py \
      mythgame/mythgame/scripts/giantbomb/giantbomb_exceptions.py

%build
%if %{with binary}
export QTDIR="%{_prefix}"
# Not gnu configure
%configure \
	--libdir-name=`basename %{_lib}` \
	--enable-all \
	%{!?with_mytharchive:--disable-mytharchive} \
	%{!?with_mythbrowser:--disable-mythbrowser} \
	%{!?with_mythgallery:--disable-mythgallery}%{?with_mythgallery:--enable-exif --enable-new-exif --enable-opengl} \
	%{!?with_mythgame:--disable-mythgame} \
	%{!?with_mythmusic:--disable-mythmusic}%{?with_mythmysic:--enable-fftw --enable-sdl --enable-aac --enable-opengl} \
	%{!?with_mythnews:--disable-mythnews} \
	%{!?with_mythweather:--disable-mythweather} \
	%{!?with_mythweb:--disable-mythweb} \
	%{!?with_mythnetvision:--disable-mythnetvision} \

mv mythconfig.mak mythconfig.mak.old
cp mythconfig.mak.old mythconfig.mak
cat <<'EOF'>> mythconfig.mak
QMAKE_CXX=%{__cxx}
QMAKE_CC=%{__cc}
OPTFLAGS=%{rpmcflags} -Wall -Wno-switch
ECFLAGS=%{rpmcflags} %{rpmcppflags} -fomit-frame-pointer
ECXXFLAGS=%{rpmcflags} %{rpmcppflags} -fomit-frame-pointer -D__STDC_CONSTANT_MACROS
EOF

%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with binary}
export QTDIR="%{_prefix}"
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/lib/{mythmusic,mythbrowser,pictures}
%if %{with mythgame}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/nes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/snes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/xmame/{roms,screens,flyers,cabs}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC/screens
cp -a mythgame/gamelist.xml $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC
%endif
%endif

%if %{with mythweb}
cd mythweb
cp -a %{SOURCE3} ./
cp -a %{SOURCE4} ./
install -d $RPM_BUILD_ROOT%{_datadir}/mythweb
install -d $RPM_BUILD_ROOT/var/cache/mythweb/{image_cache,php_sessions,tv_icons}
install -d $RPM_BUILD_ROOT%{_webapps}/%{_webapp}
cp -a *.php *.pl classes configuration includes js modules skins $RPM_BUILD_ROOT%{_datadir}/mythweb
ln -sfr $RPM_BUILD_ROOT/var/cache/mythweb $RPM_BUILD_ROOT%{_datadir}/mythweb/data
install %{SOURCE1} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/apache.conf
install %{SOURCE5} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/httpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/lighttpd.conf
touch $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/htpasswd
touch $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/htdigest
cd -
%endif

rm -f $RPM_BUILD_ROOT%{_datadir}/data
mv $RPM_BUILD_ROOT%{_datadir}/mythtv/i18n/mythbrowser_{pt_br,pt}.qm
for p in mytharchive mythbrowser mythgallery mythgame mythmusic mythnetvision mythnews mythweather mythzoneminder; do
	for l in $RPM_BUILD_ROOT%{_datadir}/mythtv/i18n/${p}_*.qm; do
		echo $l | sed -e "s,^$RPM_BUILD_ROOT\(.*${p}_\(.*\).qm\),%%lang(\2) \1,"
	done > $p.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -n mythweb -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -n mythweb -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -n mythweb -- apache-base
%webapp_register httpd %{_webapp}

%triggerin -n mythweb -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -n mythweb -- apache-base
%webapp_unregister httpd %{_webapp}

%triggerun -n mythweb -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%triggerpostun -n mythweb -- mythweb < 0.19
for i in canned_searches.php conf.php htpasswd theme_Default.php theme_compact.php theme_vxml.php theme_wap.php theme_wml.php weathertypes.dat; do
	if [ -f /etc/mythweb/$i.rpmsave ]; then
		mv -f %{_webapps}/%{_webapp}/$i{,.rpmnew}
		mv -f /etc/mythweb/$i.rpmsave %{_webapps}/%{_webapp}/$i
	fi
done
sed -i -e 's,/etc/mythweb,%{_webapps}/%{_webapp},' %{_webapps}/%{_webapp}/{apache,httpd}.conf

# migrate from apache-config macros
if [ -f /etc/mythweb/apache.conf.rpmsave ]; then
	if [ -d /etc/apache/webapps.d ]; then
		cp -f %{_webapps}/%{_webapp}/apache.conf{,.rpmnew}
		cp -f /etc/mythweb/apache.conf.rpmsave %{_webapps}/%{_webapp}/apache.conf
	fi

	if [ -d /etc/httpd/webapps.d ]; then
		cp -f %{_webapps}/%{_webapp}/httpd.conf{,.rpmnew}
		cp -f /etc/mythweb/apache.conf.rpmsave %{_webapps}/%{_webapp}/httpd.conf
	fi
	rm -f /etc/mythweb/apache.conf.rpmsave
fi

if [ -L /etc/apache/conf.d/99_mythplugins.conf ]; then
	rm -f /etc/apache/conf.d/99_mythplugins.conf
	/usr/sbin/webapp register apache %{_webapp}
	%service -q apache reload
fi
if [ -L /etc/httpd/httpd.conf/99_mythplugins.conf ]; then
	rm -f /etc/httpd/httpd.conf/99_mythplugins.conf
	/usr/sbin/webapp register httpd %{_webapp}
	%service -q httpd reload
fi

%post -n mythweb
echo "Read %{_docdir}/mythweb-%{version}/http_servers_conf_tips.txt.gz to find
which packages you can need to run mythweb and how to set it quickly."

%files
%defattr(644,root,root,755)

%if %{with mytharchive}
%files -n mytharchive -f mytharchive.lang
%defattr(644,root,root,755)
%doc mytharchive/AUTHORS mytharchive/README mytharchive/TODO
%attr(755,root,root) %{_bindir}/mytharchivehelper
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmytharchive.so
%{_datadir}/mythtv/archivemenu.xml
%{_datadir}/mythtv/archiveutils.xml
%{_datadir}/mythtv/themes/default/ma_*.png
%{_datadir}/mythtv/themes/default/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default/mythburn-ui.xml
%{_datadir}/mythtv/themes/default/mythnative-ui.xml
%{_datadir}/mythtv/themes/default-wide/mytharchive-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythburn-ui.xml
%{_datadir}/mythtv/themes/default-wide/mythnative-ui.xml
%{_datadir}/mythtv/mytharchive
%endif

%if %{with mythmusic}
%files -n mythmusic -f mythmusic.lang
%defattr(644,root,root,755)
%doc mythmusic/README mythmusic/AUTHORS mythmusic/musicdb
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythmusic.so
/var/lib/mythmusic
%{_datadir}/mythtv/musicmenu.xml
%{_datadir}/mythtv/music_settings.xml
%dir %{_datadir}/mythtv/mythmusic
%{_datadir}/mythtv/mythmusic/streams.xml
%{_datadir}/mythtv/themes/default/music-base.xml
%{_datadir}/mythtv/themes/default/music-ui.xml
%{_datadir}/mythtv/themes/default/musicsettings-ui.xml
%{_datadir}/mythtv/themes/default/mm-titlelines.png
%{_datadir}/mythtv/themes/default-wide/music-base.xml
%{_datadir}/mythtv/themes/default-wide/music-ui.xml
%{_datadir}/mythtv/themes/default-wide/musicsettings-ui.xml
%{_datadir}/mythtv/themes/default-wide/mm-titlelines.png
%{_datadir}/mythtv/themes/default-wide/stream-ui.xml
%{_datadir}/mythtv/themes/default/ff_button_off.png
%{_datadir}/mythtv/themes/default/ff_button_on.png
%{_datadir}/mythtv/themes/default/ff_button_pushed.png
%{_datadir}/mythtv/themes/default/miniplayer_background.png
%{_datadir}/mythtv/themes/default/mm_*.png
%{_datadir}/mythtv/themes/default/music-sel-bg.png
%{_datadir}/mythtv/themes/default/next_button_off.png
%{_datadir}/mythtv/themes/default/next_button_on.png
%{_datadir}/mythtv/themes/default/next_button_pushed.png
%{_datadir}/mythtv/themes/default/pause_button_off.png
%{_datadir}/mythtv/themes/default/pause_button_on.png
%{_datadir}/mythtv/themes/default/pause_button_pushed.png
%{_datadir}/mythtv/themes/default/play_button_off.png
%{_datadir}/mythtv/themes/default/play_button_on.png
%{_datadir}/mythtv/themes/default/play_button_pushed.png
%{_datadir}/mythtv/themes/default/prev_button_off.png
%{_datadir}/mythtv/themes/default/prev_button_on.png
%{_datadir}/mythtv/themes/default/prev_button_pushed.png
%{_datadir}/mythtv/themes/default/rew_button_off.png
%{_datadir}/mythtv/themes/default/rew_button_on.png
%{_datadir}/mythtv/themes/default/rew_button_pushed.png
%{_datadir}/mythtv/themes/default/selectionbar.png
%{_datadir}/mythtv/themes/default/stop_button_off.png
%{_datadir}/mythtv/themes/default/stop_button_on.png
%{_datadir}/mythtv/themes/default/stop_button_pushed.png
%{_datadir}/mythtv/themes/default/track_info_background.png
%{_datadir}/mythtv/themes/default-wide/mm_*.png
%{_datadir}/mythtv/themes/default-wide/music-sel-bg.png
%endif

%if %{with mythweather}
%files -n mythweather -f mythweather.lang
%defattr(644,root,root,755)
%doc mythweather/AUTHORS mythweather/README
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythweather.so
%{_datadir}/mythtv/mythweather
%{_datadir}/mythtv/weather_settings.xml
%{_datadir}/mythtv/themes/default/weather-ui.xml
%{_datadir}/mythtv/themes/default-wide/weather-ui.xml
%{_datadir}/mythtv/themes/default/cloudy.png
%{_datadir}/mythtv/themes/default/fair.png
%{_datadir}/mythtv/themes/default/flurries.png
%{_datadir}/mythtv/themes/default/fog.png
%{_datadir}/mythtv/themes/default/logo.png
%{_datadir}/mythtv/themes/default/lshowers.png
%{_datadir}/mythtv/themes/default/mcloudy.png
%{_datadir}/mythtv/themes/default/mw_*.png
%{_datadir}/mythtv/themes/default/mwmain.png
%{_datadir}/mythtv/themes/default/pcloudy.png
%{_datadir}/mythtv/themes/default/rainsnow.png
%{_datadir}/mythtv/themes/default/showers.png
%{_datadir}/mythtv/themes/default/snowshow.png
%{_datadir}/mythtv/themes/default/sunny.png
%{_datadir}/mythtv/themes/default/thunshowers.png
%{_datadir}/mythtv/themes/default/unknown.png
%{_datadir}/mythtv/themes/default-wide/mw-*.png
%endif

%if %{with mythgallery}
%files -n mythgallery -f mythgallery.lang
%defattr(644,root,root,755)
%doc mythgallery/AUTHORS mythgallery/README
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/themes/default/gallery-ui.xml
%{_datadir}/mythtv/themes/default-wide/gallery-ui.xml
%{_datadir}/mythtv/themes/default/gallery-*.png
/var/lib/pictures
%endif

%if %{with mythgame}
%files -n mythgame -f mythgame.lang
%defattr(644,root,root,755)
%doc mythgame/contrib
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/games
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default/game-ui.xml
%{_datadir}/mythtv/themes/default-wide/game-ui.xml
%dir %{_datadir}/mythtv/metadata/Game
%attr(755,root,root) %{_datadir}/mythtv/metadata/Game/giantbomb.py
%{_datadir}/mythtv/metadata/Game/giantbomb
%endif

%if %{with mythnews}
%files -n mythnews -f mythnews.lang
%defattr(644,root,root,755)
%doc mythnews/README mythnews/AUTHORS
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default/news-ui.xml
%{_datadir}/mythtv/themes/default/news-info-bg.png
%{_datadir}/mythtv/themes/default/enclosures.png
%{_datadir}/mythtv/themes/default/need-download.png
%{_datadir}/mythtv/themes/default/podcast.png
%{_datadir}/mythtv/themes/default-wide/news-ui.xml
%endif

%if %{with mythbrowser}
%files -n mythbrowser -f mythbrowser.lang
%defattr(644,root,root,755)
%doc mythbrowser/README mythbrowser/AUTHORS
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythbrowser.so
%{_datadir}/mythtv/themes/default/mb_*.png
%{_datadir}/mythtv/themes/default/browser-ui.xml
%{_datadir}/mythtv/themes/default-wide/browser-ui.xml
%endif

%if %{with mythweb}
%files -n mythweb
%defattr(644,root,root,755)
%doc mythweb/README mythweb/mythweb.conf.lighttpd
%doc mythweb/htdigest.sh
%doc mythweb/http_servers_conf_tips.txt
%dir %attr(750,root,http) %{_webapps}/%{_webapp}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/htpasswd
%attr(640,root,lighttpd) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/lighttpd.conf
%attr(640,root,lighttpd) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/htdigest
%{_datadir}/mythweb
%dir %attr(771,root,http) /var/cache/mythweb
%dir %attr(771,root,http) /var/cache/mythweb/image_cache
%dir %attr(771,root,http) /var/cache/mythweb/php_sessions
%dir %attr(771,root,http) /var/cache/mythweb/tv_icons
%endif

%if %{with mythnetvision}
%files -n mythnetvision -f mythnetvision.lang
%defattr(644,root,root,755)
%doc mythnetvision/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_bindir}/mythfillnetvision
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythnetvision.so
%dir %{_datadir}/mythtv/mythnetvision
%{_datadir}/mythtv/netvisionmenu.xml
%dir %{_datadir}/mythtv/mythnetvision/icons
%dir %{_datadir}/mythtv/mythnetvision/icons/directories
%{_datadir}/mythtv/mythnetvision/icons/*.png
%dir %{_datadir}/mythtv/mythnetvision/icons/directories/film_genres
%{_datadir}/mythtv/mythnetvision/icons/directories/film_genres/*.png
%dir %{_datadir}/mythtv/mythnetvision/icons/directories/music_genres
%{_datadir}/mythtv/mythnetvision/icons/directories/music_genres/*.png
%dir %{_datadir}/mythtv/mythnetvision/icons/directories/topics
%{_datadir}/mythtv/mythnetvision/icons/directories/topics/*.png
%{_datadir}/mythtv/themes/default-wide/netvision-ui.xml
%{_datadir}/mythtv/themes/default/netvision-ui.xml
%endif

%if %{with mythzoneminder}
%files -n mythzoneminder
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%doc mythzoneminder/{AUTHORS,README}
%attr(755,root,root) %{_bindir}/mythzmserver
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythzoneminder.so
%{_datadir}/mythtv/zonemindermenu.xml
%{_datadir}/mythtv/themes/default/zoneminder-ui.xml
%{_datadir}/mythtv/themes/default-wide/zoneminder-ui.xml
%{_datadir}/mythtv/themes/default/mz_*png
%{_datadir}/mythtv/i18n/mythzoneminder_*.qm
%endif
