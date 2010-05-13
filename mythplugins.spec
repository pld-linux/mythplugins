#
# Conditional build:
%bcond_without	binary		# skip building binary plugins (build only mythweb)
%bcond_without	mytharchive	# disable mytharchive plugin
%bcond_without	mythbrowser	# disable building mythbrowser plugin
%bcond_without	mythmovies	# disable mythmovies plugin
%bcond_without	mythdvd		# mythvideo part
%bcond_without	mythnetvision	# disable building mythnetvision plugin
%bcond_without	mythgallery	# disable building mythgallery plugin
%bcond_without	mythgame	# disable building mythgallery plugin
%bcond_without	mythmusic	# disable building mythmusic plugin
%bcond_without	mythnews	# disable building mythgallery plugin
%bcond_without	mythvideo	# disable building mythgallery plugin
%bcond_without	mythweather	# building mythgallery plugin disabled by default
				# it looks unusable "due to msnbc webpage structure change
%bcond_without	mythweb		# disable building mythgallery plugin
%bcond_without  mythzoneminder  # disable building mythzoneminder plugin

%if !%{with binary}
%undefine	with_mytharchive
%undefine	with_mythbrowser
%undefine	with_mythmovies
%undefine	with_mythdvd
%undefine	with_mythnetvision
%undefine	with_mythgallery
%undefine	with_mythgame
%undefine	with_mythmusic
%undefine	with_mythnews
%undefine	with_mythvideo
%undefine	with_mythweather
%endif

%include	/usr/lib/rpm/macros.perl

#%define fix     24635

Summary:	Main MythTV plugins
Summary(pl.UTF-8):	Główne wtyczki MythTV
Name:		mythplugins
Version:	0.23
#Release:	fix%{fix}.1
Release:	0.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	ftp://ftp.osuosl.org/pub/mythtv/%{name}-%{version}.tar.bz2
# Source0-md5:	be44db841f9e03d0d17ab449545b38aa
Source1:	mythweb.conf
#Patch0: %{name}-lib64.patch
#Patch1: %{name}-paths.patch
Patch2:		mythweb-chdir.patch
Patch20:	%{name}-mytharchive-INT64.patch
#Patch21:	mythmusic_fftw3.patch
#Patch100:	mythtv-branch.diff
URL:		http://www.mythtv.org/
%if %{with binary}
%if %{with mythgallery} || %{with myhtmusic}
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
BuildRequires:	cdparanoia-III-devel
BuildRequires:	faad2-devel >= 2.0-5.2
%{?with_mythmusic:BuildRequires:	fftw-devel >= 2.1.3}
BuildRequires:	flac-devel >= 1.0.4
BuildRequires:	freetype-devel
BuildRequires:	libcdaudio-devel >= 0.99.12p2
BuildRequires:	libdvdcss-devel >= 1.2.7
BuildRequires:	libdvdread-devel >= 0.9.4
%{?with_mythgallery:BuildRequires:	libexif-devel >= 1:0.6.9}
BuildRequires:	libfame-devel >= 0.9.0
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmyth-devel > 0.21
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	mjpegtools-devel >= 1.6.1
BuildRequires:	nasm
BuildRequires:	patchutils
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
%{?with_mythmusic:BuildRequires:        taglib-devel}
%{?with_mythdvd:BuildRequires:	transcode >= 0.6.8}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xvid-devel >= 1:0.9.1
BuildRequires:	zlib-devel
%endif
%{?with_mytharchive:Requires:	mytharchive}
%{?with_mythbrowser:Requires:	mythbrowser}
%{?with_mythdvd:Requires:	mythdvd}
%{?with_mythnetvision:Requires:	mythnetvision}
%{?with_mythgallery:Requires:	mythgallery}
%{?with_mythgame:Requires:	mythgame}
%{?with_mythmysic:Requires:	mythmusic}
%{?with_mythnews:Requires:	mythnews}
%{?with_mythvideo:Requires:	mythvideo}
%{?with_mythweather:Requires:	mythweather}
%{?with_mythweb:Requires:	mythweb}
ExclusiveArch:	%{ix86} %{x8664} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		myth_api_version %(awk '/LIBVERSION/{print $3}' %{_datadir}/mythtv/build/settings.pro 2>/dev/null || echo ERROR)
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
BuildRequires:	libvisual-devel
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythmusic
Music add-on for MythTV.

%description -n mythmusic -l pl.UTF-8
Odtwarzacz muzyki dla MythTV.

%package -n mythvideo
Summary:	A generic video player frontend module for MythTV
Summary(pl.UTF-8):	Moduł ogólnego interfejsu do odtwarzania obrazu dla MythTV
Group:		Applications/Multimedia
Requires:	mplayer
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythvideo
A generic video and dvd player frontend module for MythTV.

%description -n mythvideo -l pl.UTF-8
Moduł ogólnego interfejsu do odtwarzania obrazu dla MythTV.

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

%package -n mythdvd
Summary:	A DVD ripper module for MythTV
Summary(pl.UTF-8):	Moduł rippujący DVD dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}
Requires:	mythvideo
Requires:	transcode >= 0.6.8

%description -n mythdvd
MythDVD is a MythTV module that allows you to rip DVD's and transcode
their video and audio content to other (generally smaller) formats.
The playing features are simply myth-style wrappers for your favourite
DVD playing software (mplayer, ogle, xine, etc). The transcoding is
based on and derived from the excellent transcode package.

%description -n mythdvd -l pl.UTF-8
MythDVD to moduł MythTV umożliwiający rippowanie DVD oraz
przekodowywanie obrazu i dźwięku do innych (zwykle mniej zajmujących)
formatów. Możliwości odtwarzania to po prostu obudowanie w stylu myth
dla ulubionego oprogramowania do odtwarzania DVD (mplayer, ogle, xine
itp.). Przekodowywanie jest oparte i wywodzi się ze wspaniałego
pakietu transcode.

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
#Suggests:	apache(mod_auth)
#Suggests:	apache(mod_env)

%description -n mythweb
The web interface to MythTV.

%description -n mythweb -l pl.UTF-8
Interfejs WWW do MythTV.

%package -n mythnetvision
Summary:	Mythtv extension to watch network movie shows
Summary(pl.UTF-8):	Dodatek do MythTV do oglądania sieciowych transmisji
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythnetvision
Mythtv extension to watch network movie shows (ex. YouTube).

%description -n mythnetvision -l pl.UTF-8
Dodatek do MythTV do oglądania sieciowych transmisji.
Na przykład z YouTube.

%package -n mythmovies
Summary:	MythTV cinemas timetable
Summary(pl.UTF-8):	Moduł MythTV do repertuaru kinowego
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{myth_api_version}

%description -n mythmovies
MythTV cinemas timetable.


%description -n mythmovies -l pl.UTF-8
Moduł MythTV do repertuaru kinowego.

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
%setup -q -n %{name}-%{version}
#%if %{_lib} != "lib"
#%patch0 -p1
#%endif
#%patch1 -p1
%patch2 -p1
%patch20 -p1
#%patch21 -p1
#filterdiff -i 'mythplugins/*' %{PATCH100} | %{__patch} -p1 -s

# make it visible
#mv mythweb/data/{.,}htaccess

# lib64 fix - enable to update patch
%if %{_lib} != "lib" && 0
find '(' -name '*.[ch]' -o -name '*.cpp' -o -name '*.pro' ')' | \
xargs grep -l /lib/ . | xargs sed -i -e '
	s,/usr/lib/,/%{_lib}/,g
	s,{PREFIX}/lib,{PREFIX}/%{_lib},g
'
exit 1
%endif

%build
%if %{with binary}
export QTDIR="%{_prefix}"
# Not gnu configure
%configure \
	--libdir-name=`basename %{_lib}` \
	--enable-all \
	%{!?with_mytharchive:--disable-mytharchive} \
	%{!?with_mythbrowser:--disable-mythbrowser} \
	%{!?with_mythdvd:--disable-mythdvd}%{?with_mythdvd:--enable-transcode --enable-vcd} \
	%{!?with_mythgallery:--disable-mythgallery}%{?with_mythgallery:--enable-exif --enable-new-exif --enable-opengl} \
	%{!?with_mythgame:--disable-mythgame} \
	%{!?with_mythmusic:--disable-mythmusic}%{?with_mythmysic:--enable-fftw --enable-sdl --enable-aac --enable-opengl} \
	%{!?with_mythnews:--disable-mythnews} \
	%{!?with_mythvideo:--disable-mythvideo} \
	%{!?with_mythweather:--disable-mythweather} \
	%{!?with_mythweb:--disable-mythweb} \
	%{!?with_mythmovies:--disable-mythmovies} \
	%{!?with_mythnetvision:--disable-mythnetvision} \

mv mythconfig.mak mythconfig.mak.old
cp mythconfig.mak.old mythconfig.mak
cat <<'EOF'>> mythconfig.mak
QMAKE_CXX=%{__cxx}
QMAKE_CC=%{__cc}
OPTFLAGS=%{rpmcflags} -Wall -Wno-switch
ECFLAGS=%{rpmcflags} -fomit-frame-pointer
ECXXFLAGS=%{rpmcflags} -fomit-frame-pointer
EOF

%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with binary}
export QTDIR="%{_prefix}"
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/lib/{mythmusic,mythbrowser,mythvideo,pictures}
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
install -d $RPM_BUILD_ROOT%{_datadir}/mythweb
install -d $RPM_BUILD_ROOT/var/cache/mythweb/{image_cache,php_sessions,tv_icons}
install -d $RPM_BUILD_ROOT%{_webapps}/%{_webapp}
cp -a *.php *.pl classes configuration includes js modules skins $RPM_BUILD_ROOT%{_datadir}/mythweb
ln -sf /var/cache/mythweb $RPM_BUILD_ROOT%{_datadir}/data
install %{SOURCE1} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/httpd.conf
touch $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/htpasswd
cd -
%endif

rm -f $RPM_BUILD_ROOT%{_datadir}/data
mv $RPM_BUILD_ROOT%{_datadir}/mythtv/i18n/mythbrowser_{pt_br,pt}.qm
for p in mytharchive mythbrowser mythmovies mythdvd mythgallery mythgame mythmusic mythnews mythnetvision mythvideo mythweather mythzoneminder; do
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

%triggerin -n mythweb -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -n mythweb -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

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

%files
%defattr(644,root,root,755)

%if %{with mytharchive}
%files -n mytharchive -f mytharchive.lang
%defattr(644,root,root,755)
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
%{_datadir}/mythtv/themes/default/music-ui.xml
%{_datadir}/mythtv/themes/default/mm-titlelines.png
%{_datadir}/mythtv/themes/default-wide/music-ui.xml
%{_datadir}/mythtv/themes/default-wide/mm-titlelines.png
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

%if %{with mythvideo}
%files -n mythvideo -f mythvideo.lang
%defattr(644,root,root,755)
%doc mythvideo/README mythvideo/videodb
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythvideo.so
%{_datadir}/mythtv/themes/default/video-ui.xml
%{_datadir}/mythtv/themes/default-wide/video-ui.xml
%{_datadir}/mythtv/themes/default/mv_*.png
%{_datadir}/mythtv/themes/default-wide/mv_*.png
%{_datadir}/mythtv/video_settings.xml
%{_datadir}/mythtv/videomenu.xml
%dir %{_datadir}/mythtv/mythvideo
%dir %{_datadir}/mythtv/mythvideo/scripts
%dir %{_datadir}/mythtv/mythvideo/scripts/Movie
%dir %{_datadir}/mythtv/mythvideo/scripts/Movie/MythTV
%dir %{_datadir}/mythtv/mythvideo/scripts/Television
%{_datadir}/mythtv/mythvideo/scripts/README
%{_datadir}/mythtv/mythvideo/scripts/jamu.README
%{_datadir}/mythtv/mythvideo/scripts/jamu-example.conf
%attr(755,root,root) %{_datadir}/mythtv/mythvideo/scripts/Movie/*.pl
%attr(755,root,root) %{_datadir}/mythtv/mythvideo/scripts/Movie/*.py
%attr(644,root,root) %{_datadir}/mythtv/mythvideo/scripts/Movie/MythTV/*
%attr(755,root,root) %{_datadir}/mythtv/mythvideo/scripts/*.py
%attr(644,root,root) %{_datadir}/mythtv/mythvideo/scripts/Television/*
/var/lib/mythvideo
%endif

%if %{with mythweather}
%files -n mythweather -f mythweather.lang
%defattr(644,root,root,755)
%doc mythweather/README
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
%doc mythgallery/README
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/themes/default/gallery-ui.xml
%{_datadir}/mythtv/themes/default-wide/gallery-ui.xml
%{_datadir}/mythtv/themes/default/gallery-*.png
# FIXME: this is definately stupid path
/var/lib/pictures
%endif

%if %{with mythgame}
%files -n mythgame -f mythgame.lang
%defattr(644,root,root,755)
#%doc mythgame/README
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/games
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default/game-ui.xml
%{_datadir}/mythtv/themes/default-wide/game-ui.xml
%endif

%if %{with mythdvd}
%files -n mythdvd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mtd
%{_datadir}/mythtv/themes/default/dvd-ui.xml
%{_datadir}/mythtv/themes/default-wide/dvd-ui.xml
%{_datadir}/mythtv/themes/default/md_*.png
%endif

%if %{with mythnews}
%files -n mythnews -f mythnews.lang
%defattr(644,root,root,755)
%doc mythnews/README mythnews/AUTHORS
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default/news-ui.xml
# DUPLICATE WITH MYTHFLIX?
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
#%attr(755,root,root) %{_bindir}/mythbrowser
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythbrowser.so
%{_datadir}/mythtv/themes/default/mb_progress*.png
%{_datadir}/mythtv/themes/default/browser-ui.xml
%{_datadir}/mythtv/themes/default-wide/browser-ui.xml
%endif

%if %{with mythweb}
%files -n mythweb
%defattr(644,root,root,755)
%doc mythweb/README mythweb/mythweb.conf.lighttpd
#%doc mythweb/data/htaccess
%dir %attr(750,root,http) %{_webapps}/%{_webapp}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/httpd.conf
#%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/*.php
#%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/*.dat
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/htpasswd
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
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythnetvision.so
%dir %{_datadir}/mythtv/mythnetvision
%{_datadir}/mythtv/netvisionmenu.xml
%dir %{_datadir}/mythtv/mythnetvision/scripts
%attr(755,root,root) %{_datadir}/mythtv/mythnetvision/scripts/twit.tv.pl
%dir %{_datadir}/mythtv/mythnetvision/icons
%dir %{_datadir}/mythtv/mythnetvision/icons/directories
%{_datadir}/mythtv/mythnetvision/icons/*.png
%{_datadir}/mythtv/mythnetvision/icons/vimeo.jpg
%{_datadir}/mythtv/mythnetvision/icons/directories/film_genres/*.png
%{_datadir}/mythtv/mythnetvision/icons/directories/music_genres/*.png
%{_datadir}/mythtv/mythnetvision/icons/directories/topics/*.png
%attr(755,root,root) %{_datadir}/mythtv/mythnetvision/scripts/*.py
%dir %{_datadir}/mythtv/mythnetvision/scripts/nv_python_libs
%{_datadir}/mythtv/mythnetvision/scripts/nv_python_libs/*
%{_datadir}/mythtv/themes/default-wide/netvision-ui.xml   
%{_datadir}/mythtv/themes/default/netvision-ui.xml
%endif

%if %{with mythmovies}
%files -n mythmovies
%defattr(644,root,root,755)
#-f mythmovies.lang
%defattr(644,root,root,755)
%doc mythmovies/{README,TODO}
%attr(755,root,root) %{_bindir}/ignyte
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythmovies.so
%{_datadir}/mythtv/themes/default/movies-ui.xml
%{_datadir}/mythtv/themes/default-wide/movies-ui.xml
%{_datadir}/mythtv/i18n/mythmovies_*.qm
%endif

%if %{with mythzoneminder}
%files -n mythzoneminder
%defattr(644,root,root,755)
#-f mythmovies.lang
%defattr(644,root,root,755)
%doc mythzoneminder/{AUTHORS,README}
%attr(755,root,root) %{_bindir}/mythzmserver
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythzoneminder.so
%dir %{_datadir}/mythtv/zonemindermenu.xml
%{_datadir}/mythtv/themes/default/zoneminder-ui.xml
%{_datadir}/mythtv/themes/default-wide/zoneminder-ui.xml
%{_datadir}/mythtv/themes/default/mz_*png
%{_datadir}/mythtv/i18n/mythzoneminder_*.qm
%endif
