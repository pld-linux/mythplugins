# Conditional build:
%bcond_without	binary		# skip building binary plugins (build only mythweb)
%bcond_without	mythbrowser	# disable building mythbrowser plugin
%bcond_without	mythdvd		# disable building mythgallery plugin
%bcond_without	mythgallery	# disable building mythgallery plugin
%bcond_without	mythgame	# disable building mythgallery plugin
%bcond_without	mythmusic	# disable building mythmusic plugin
%bcond_without	mythnews	# disable building mythgallery plugin
%bcond_without	mythphone	# disable building mythgallery plugin
%bcond_without	mythvideo	# disable building mythgallery plugin
%bcond_without	mythweather	# disable building mythgallery plugin
%bcond_without	mythweb		# disable building mythgallery plugin
%bcond_without	mythflix	# disable building mythflix plugin
%bcond_without	mythcontrols	# disable mythcontrols plugin
#
%if %{without binary}
%undefine	with_mythbrowser
%undefine	with_mythdvd
%undefine	with_mythgallery
%undefine	with_mythgame
%undefine	with_mythmusic
%undefine	with_mythnews
%undefine	with_mythphone
%undefine	with_mythvideo
%undefine	with_mythweather
%undefine	with_mythcontrols
%undefine	with_mythflix
%endif

%include	/usr/lib/rpm/macros.perl

%define	_snap 20060204
%define	_rev 8859
%define	_rel 1
Summary:	Main MythTV plugins
Summary(pl):	G³ówne wtyczki MythTV
Name:		mythplugins
Version:	0.19
Release:	0.%{_snap}.%{_rev}.%{_rel}
License:	GPL v2
Group:		Applications/Multimedia
#Source0:	http://www.mythtv.org/mc/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{_snap}.%{_rev}.tar.bz2
# Source0-md5:	8bc1d93b2c92c6c47b4038e5162e8167
Source1:	mythweb.conf
Patch0:		%{name}-lib64.patch
Patch1:		%{name}-paths.patch
Patch2:		mythweb-config.patch
URL:		http://www.mythtv.org/
%if %{with binary}
%if %{with mythgallery} || %{with myhtmusic}
BuildRequires:	OpenGL-devel
%endif
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	a52dec-libs-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	faad2-devel >= 2.0-5.2
%{?with_mythmusic:BuildRequires:	fftw-devel >= 2.1.3}
BuildRequires:	flac-devel >= 1.0.4
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libcdaudio-devel
BuildRequires:	libdvdcss-devel >= 1.2.7
BuildRequires:	libdvdread-devel >= 0.9.4
%{?with_mythgallery:BuildRequires:	libexif-devel >= 1:0.6.9}
BuildRequires:	libfame-devel >= 0.9.0
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmyth-devel >= 0.19
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	mjpegtools-devel >= 1.6.1
BuildRequires:	nasm
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
%{?with_mythdvd:BuildRequires:	transcode >= 0.6.8}
BuildRequires:	xvid-devel >= 1:0.9.1
BuildRequires:	zlib-devel
%endif
%{?with_mythbrowser:Requires:	mythbrowser}
%{?with_mythdvd:Requires:	mythdvd}
%{?with_mythflix:Requires:	mythflix}
%{?with_mythgallery:Requires:	mythgallery}
%{?with_mythgame:Requires:	mythgame}
%{?with_mythmysic:Requires:	mythmusic}
%{?with_mythnews:Requires:	mythnews}
%{?with_mythphone:Requires:	mythphone}
%{?with_mythvideo:Requires:	mythvideo}
%{?with_mythweather:Requires:	mythweather}
%{?with_mythweb:Requires:	mythweb}
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		api_ver %(awk '/LIBVERSION/{print $3}' %{_datadir}/mythtv/build/settings.pro 2>/dev/null || echo ERROR)
%define		_webapps	/etc/webapps
%define		_webapp		mythweb

%description
This is a consolidation of all the official MythTV plugins that used
to be distributed as separate downloads from mythtv.org.

%description -l pl
Jest to zbiór wszystkich oficjalnych wtyczek MythTV, które by³y
wcze¶niej rozpowszechniane jako osobne pakiety na mythtv.org.

%package -n mythmusic
Summary:	The music player add-on module for MythTV
Summary(pl):	Modu³ odtwarzacza muzyki dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythmusic
Music add-on for MythTV.

%description -n mythmusic -l pl
Odtwarzacz muzyki dla MythTV.

%package -n mythvideo
Summary:	A generic video player frontend module for MythTV
Summary(pl):	Modu³ ogólnego interfejsu do odtwarzania obrazu dla MythTV
Group:		Applications/Multimedia
Requires:	mplayer
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythvideo
A generic video player frontend module for MythTV.

%description -n mythvideo -l pl
Modu³ ogólnego interfejsu do odtwarzania obrazu dla MythTV.

%package -n mythweather
Summary:	A MythTV module that displays a weather forcast
Summary(pl):	Modu³ MythTV wy¶wietlaj±cy prognozê pogody
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythweather
A MythTV module that displays a weather forcast.

%description -n mythweather -l pl
Modu³ MythTV wy¶wietlaj±cy prognozê pogody.

%package -n mythgallery
Summary:	A gallery/slideshow module for MythTV
Summary(pl):	Modu³ galerii/pokazu slajdów dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythgallery
A gallery/slideshow module for MythTV.

%description -n mythgallery -l pl
Modu³ galerii/pokazu slajdów dla MythTV.

%package -n mythgame
Summary:	A game frontend (xmame, nes, snes, pc) for MythTV
Summary(pl):	Interfejs do gier (xmame, nes, snes, pc) dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythgame
A game frontend (xmame, nes, snes, pc) for MythTV.

%description -n mythgame -l pl
Interfejs do gier (xmame, nes, snes, pc) dla MythTV.

%package -n mythdvd
Summary:	A DVD player module for MythTV
Summary(pl):	Modu³ odtwarzacza DVD dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}
Requires:	transcode >= 0.6.8

%description -n mythdvd
MythDVD is a MythTV module that allows you to play DVDs on a myth-box
and (optionally) rip DVD's and transcode their video and audio content
to other (generally smaller) formats. The playing features are simply
myth-style wrappers for your favourite DVD playing software (mplayer,
ogle, xine, etc). The transcoding is based on and derived from the
excellent transcode package.

%description -n mythdvd -l pl
MythDVD to modu³ MythTV umo¿liwiaj±cy odtwarzanie p³yt DVD w MythTV i
(opcjonalnie) rippowanie ich oraz przekodowywanie obrazu i d¼wiêku do
innych (zwykle mniej zajmuj±cych) formatów. Mo¿liwo¶ci odtwarzania to
po prostu obudowanie w stylu myth dla ulubionego oprogramowania do
odtwarzania DVD (mplayer, ogle, xine itp.). Przekodowywanie jest
oparte i wywodzi siê z wspania³ego pakietu transcode.

%package -n mythnews
Summary:	A RSS News Feed plugin for MythTV
Summary(pl):	Wtyczka czytnika nowinek RSS dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythnews
A RSS News Feed plugin for MythTV.

%description -n mythnews -l pl
Wtyczka czytnika nowinek RSS dla MythTV.

%package -n mythbrowser
Summary:	A small web browser module for MythTV
Summary(pl):	Modu³ ma³ej przegl±darki WWW dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythbrowser
MythBrowser is a full fledged web-browser (multiple tabs) to display
webpages in full-screen mode. Simple page navigation is possible.
Starting with version 0.13 it also has full support for mouse driven
navigation (right mouse opens and closes the popup menu).

MythBrowser also contains a BookmarkManager to manage the website
links in a simple mythplugin.

%description -n mythbrowser -l pl
MythBrowser to w pe³ni funkcjonalna przegl±darka WWW (z wieloma
zak³adkami) wy¶wietlaj±ca strony WWW w trybie pe³noekranowym. Mo¿liwa
jest prosta nawigacja po stronie. Pocz±wszy od wersji 0.13 ma pe³n±
obs³ugê nawigacji myszk± (prawy przycisk otwiera i zamywa wyskakuj±ce
menu).

MythBrowser zawiera tak¿e BookmarkManagera do zarz±dzania odno¶nikami
do stron w prostej wtyczce myth.

%package -n mythphone
Summary:	A video conferencing module for MythTV
Summary(pl):	Modu³ wideokonferencji dla MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythphone
Mythphone is a phone and videophone capability on Myth using the
standard SIP protocol. It is compatible with Microsoft XP Messenger
and with SIP Service Providers such as Free World Dialup
(fwd.pulver.com).

%description -n mythphone -l pl
Mythphone to funkcjonalno¶æ telefonu i wideofonu w Myth przy u¿yciu
standardowego protoko³u SIP. Jest kompatybilny z Microsoft XP
Messengerem oraz dostawcami us³ug SIP, takimi jak Free World Dialup
(fwd.pulver.com).

%package -n mythweb
Summary:	The web interface to MythTV
Summary(pl):	Interfejs WWW do MythTV
Group:		Applications/Multimedia
Requires:	webapps
#Suggests:	apache(mod_auth)
#Suggests:	apache(mod_env)
Requires:	php >= 3:4.3
Requires:	php-mysql
Requires:	php-posix

%description -n mythweb
The web interface to MythTV.

%description -n mythweb -l pl
Interfejs WWW do MythTV.

%package -n mythflix
Summary:	MythFlix (A NetFlix MythTV)
Summary(pl):	MythFlix (NetFlix MythTV)
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythflix
MythFlix is a MythTV plugin for adding movies to your Netflix queue.
It currently supports the ability to view your queue and add movies to
your queue. The browse feature is based on the Netflix RSS feeds. This
plugin is not very mature, which means things might not work right
and/or it might break other things.

%description -n mythflix -l pl
MythFlix to wtyczka MythTV do dodawania filmów do kolejki Netfliksa.
Aktualnie daje mo¿liwo¶æ ogl±dania kolejki i dodawania do niej filmów.
Przegl±danie jest oparte na kanale RSS Netfliksa. Ta wtyczka nie jest
jeszcze zbyt dojrza³a, co znaczy, ¿e co¶ mo¿e nie dzia³aæ lub psuæ co¶
innego.

%package -n mythcontrols
Summary:	MythTV keybindings editor
Summary(pl):	Edytor przypisañ klawiszy MythTV
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythcontrols
This plugin allows you to configure your keybindings on the frontend
without having to use mythweb or edit tables by hand.

%description -n mythcontrols -l pl
Ta wtyczka pozwala konfigurowaæ przypisania klawiszy we frontendzie
bez konieczno¶ci u¿ywania mythweba ani rêcznego modyfikowania tabel.

%prep
%setup -q %{?_snap:-n %{name}}
%if %{_lib} != "lib"
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

# make it visible
mv mythweb/{.,}htaccess

# lib64 fix - enable to update patch
%if %{_lib} != "lib" && 0
find '(' -name '*.[ch]' -o -name '*.cpp' -o -name '*.pro' ')' | \
xargs grep -l /lib/ . | xargs sed -i -e '
	s,/usr/lib/,/usr/%{_lib}/,g
	s,{PREFIX}/lib,{PREFIX}/%{_lib},g
'
exit 1
%endif

%build
%if %{with binary}
export QTDIR="%{_prefix}"
# Not gnu configure
%configure \
	--enable-all \
	%{!?with_mythbrowser:--disable-mythbrowser} \
	%{!?with_mythdvd:--disable-mythdvd}%{?with_mythdvd:--enable-transcode --enable-vcd} \
	%{!?with_mythgallery:--disable-mythgallery}%{?with_mythgallery:--enable-exif --enable-new-exif --enable-opengl} \
	%{!?with_mythgame:--disable-mythgame} \
	%{!?with_mythmusic:--disable-mythmusic}%{?with_mythmysic:--enable-fftw --enable-sdl --enable-aac --enable-opengl} \
	%{!?with_mythnews:--disable-mythnews} \
	%{!?with_mythphone:--disable-mythphone}%{?with_mythphone:--disable-festival} \
	%{!?with_mythvideo:--disable-mythvideo} \
	%{!?with_mythweather:--disable-mythweather} \
	%{!?with_mythweb:--disable-mythweb} \
	%{!?with_mythcontrols:--disable-mythcontrols} \
	%{!?with_mythflix:--disable-mythflix} \

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

install -d $RPM_BUILD_ROOT/var/lib/{mythmusic,mythvideo,pictures}
%if %{with mythgame}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/nes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/snes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/xmame/{roms,screens,flyers,cabs}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC/screens
cp -a mythgame/gamelist.xml $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC
%endif
%endif

%if %{with mythweb}
install -d $RPM_BUILD_ROOT%{_datadir}/mythweb/{includes,languages}
install -d $RPM_BUILD_ROOT/var/cache/mythweb/{image_cache,php_sessions,tv_icons}
install -d $RPM_BUILD_ROOT%{_webapps}/%{_webapp}
cp -a mythweb/*.php $RPM_BUILD_ROOT%{_datadir}/mythweb
cp -a mythweb/languages/*.php $RPM_BUILD_ROOT%{_datadir}/mythweb/languages
cp -a mythweb/includes/*.php $RPM_BUILD_ROOT%{_datadir}/mythweb/includes
cp -a mythweb/{images,js,skins,modules,themes,templates} $RPM_BUILD_ROOT%{_datadir}/mythweb
cp -a mythweb/config/*.{php,dat} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}
install %{SOURCE1} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/httpd.conf
touch $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/htpasswd
%endif

for p in mythmusic mythvideo mythweather mythgallery mythgame mythdvd mythnews mythbrowser mythphone mythflix mythcontrols; do
	for l in $RPM_BUILD_ROOT%{_datadir}/mythtv/i18n/${p}_*.qm; do
		echo $l | sed -e "s,^$RPM_BUILD_ROOT\(.*${p}_\(.*\).qm\),%%lang(\2) \1,"
	done > $p.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -n mythweb -- apache1
%webapp_register apache %{_webapp}

%triggerun -n mythweb -- apache1
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

%if %{with mythmusic}
%files -n mythmusic -f mythmusic.lang
%defattr(644,root,root,755)
%doc mythmusic/README mythmusic/UPGRADING mythmusic/AUTHORS mythmusic/musicdb
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythmusic.so
/var/lib/mythmusic
%{_datadir}/mythtv/musicmenu.xml
%{_datadir}/mythtv/music_settings.xml
%{_datadir}/mythtv/themes/default/music-ui.xml
%{_datadir}/mythtv/themes/default/ff_button_off.png
%{_datadir}/mythtv/themes/default/ff_button_on.png
%{_datadir}/mythtv/themes/default/ff_button_pushed.png
%{_datadir}/mythtv/themes/default/mm_blackhole_border.png
%{_datadir}/mythtv/themes/default/mm_blankbutton_off.png
%{_datadir}/mythtv/themes/default/mm_blankbutton_on.png
%{_datadir}/mythtv/themes/default/mm_blankbutton_pushed.png
%{_datadir}/mythtv/themes/default/mm_checked.png
%{_datadir}/mythtv/themes/default/mm_checked_high.png
%{_datadir}/mythtv/themes/default/mm_down_arrow.png
%{_datadir}/mythtv/themes/default/mm_left_arrow.png
%{_datadir}/mythtv/themes/default/mm_leftright_off.png
%{_datadir}/mythtv/themes/default/mm_leftright_on.png
%{_datadir}/mythtv/themes/default/mm_leftright_pushed.png
%{_datadir}/mythtv/themes/default/mm_rating.png
%{_datadir}/mythtv/themes/default/mm_right_arrow.png
%{_datadir}/mythtv/themes/default/mm_unchecked.png
%{_datadir}/mythtv/themes/default/mm_unchecked_high.png
%{_datadir}/mythtv/themes/default/mm_up_arrow.png
%{_datadir}/mythtv/themes/default/mm_volume_background.png
%{_datadir}/mythtv/themes/default/mm_volume_tick.png
%{_datadir}/mythtv/themes/default/mm_waiting.png
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
%{_datadir}/mythtv/themes/default/text_button_off.png
%{_datadir}/mythtv/themes/default/text_button_on.png
%{_datadir}/mythtv/themes/default/text_button_pushed.png
%{_datadir}/mythtv/themes/default/track_info_background.png
%endif

%if %{with mythvideo}
%files -n mythvideo -f mythvideo.lang
%defattr(644,root,root,755)
%doc mythvideo/README mythvideo/UPGRADING mythvideo/videodb
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythvideo.so
%{_datadir}/mythtv/themes/default/video-ui.xml
%{_datadir}/mythtv/themes/default/mv-*.png
%{_datadir}/mythtv/themes/default/mv_*.png
%{_datadir}/mythtv/video_settings.xml
%{_datadir}/mythtv/videomenu.xml
%dir %{_datadir}/mythtv/mythvideo
%dir %{_datadir}/mythtv/mythvideo/scripts
%{_datadir}/mythtv/mythvideo/scripts/README
%attr(755,root,root) %{_datadir}/mythtv/mythvideo/scripts/imdb.pl
%attr(755,root,root) %{_datadir}/mythtv/mythvideo/scripts/allocine.pl
%attr(755,root,root) %{_datadir}/mythtv/mythvideo/scripts/ofdb.pl
/var/lib/mythvideo

%endif

%if %{with mythweather}
%files -n mythweather -f mythweather.lang
%defattr(644,root,root,755)
%doc mythweather/README
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythweather.so
%{_datadir}/mythtv/mythweather
%{_datadir}/mythtv/themes/default/weather-ui.xml
%{_datadir}/mythtv/themes/default/cloudy.png
%{_datadir}/mythtv/themes/default/fair.png
%{_datadir}/mythtv/themes/default/flurries.png
%{_datadir}/mythtv/themes/default/fog.png
%{_datadir}/mythtv/themes/default/logo.png
%{_datadir}/mythtv/themes/default/lshowers.png
%{_datadir}/mythtv/themes/default/mcloudy.png
%{_datadir}/mythtv/themes/default/mw-*.png
%{_datadir}/mythtv/themes/default/mwmain.png
%{_datadir}/mythtv/themes/default/pcloudy.png
%{_datadir}/mythtv/themes/default/rainsnow.png
%{_datadir}/mythtv/themes/default/showers.png
%{_datadir}/mythtv/themes/default/snowshow.png
%{_datadir}/mythtv/themes/default/sunny.png
%{_datadir}/mythtv/themes/default/thunshowers.png
%{_datadir}/mythtv/themes/default/unknown.png
%endif

%if %{with mythgallery}
%files -n mythgallery -f mythgallery.lang
%defattr(644,root,root,755)
%doc mythgallery/README mythgallery/UPGRADING
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/themes/default/gallery-ui.xml
%{_datadir}/mythtv/themes/default/gallery-*.png
# FIXME: this is definately stupid path
/var/lib/pictures
%endif

%if %{with mythgame}
%files -n mythgame -f mythgame.lang
%defattr(644,root,root,755)
%doc mythgame/README mythgame/UPGRADING
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/games
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default/game-ui.xml
%endif

%if %{with mythdvd}
%files -n mythdvd -f mythdvd.lang
%defattr(644,root,root,755)
%doc mythdvd/README mythdvd/UPGRADING mythdvd/AUTHORS
%attr(755,root,root) %{_bindir}/mtd
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythdvd.so
%{_datadir}/mythtv/dvd_settings.xml
%{_datadir}/mythtv/dvdmenu.xml
%{_datadir}/mythtv/themes/default/dvd-ui.xml
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
%endif

%if %{with mythbrowser}
%files -n mythbrowser -f mythbrowser.lang
%defattr(644,root,root,755)
%doc mythbrowser/README mythbrowser/AUTHORS
%attr(755,root,root) %{_bindir}/mythbrowser
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythbookmarkmanager.so
%{_datadir}/mythtv/themes/default/webpage.png
%endif

%if %{with mythphone}
%files -n mythphone -f mythphone.lang
%defattr(644,root,root,755)
%doc mythphone/README mythphone/AUTHORS mythphone/TODO
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythphone.so
%{_datadir}/mythtv/themes/default/phone-ui.xml
%{_datadir}/mythtv/themes/default/webcam-ui.xml
%{_datadir}/mythtv/themes/default/mp_*.png
%{_datadir}/mythtv/themes/default/phone.png
%endif

%if %{with mythweb}
%files -n mythweb
%defattr(644,root,root,755)
%doc mythweb/{README,TODO} mythweb/languages/*.{pl,txt}
%dir %attr(750,root,http) %{_webapps}/%{_webapp}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/*.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/*.dat
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/htpasswd
%{_datadir}/mythweb
%dir %attr(771,root,http) /var/cache/mythweb
%dir %attr(771,root,http) /var/cache/mythweb/image_cache
%dir %attr(771,root,http) /var/cache/mythweb/php_sessions
%dir %attr(771,root,http) /var/cache/mythweb/tv_icons
%endif

%if %{with mythflix}
%files -n mythflix -f mythflix.lang
%defattr(644,root,root,755)
%doc mythflix/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythflix.so
%dir %{_datadir}/mythtv/mythflix
%{_datadir}/mythtv/mythflix/netflix-rss.xml
%dir %{_datadir}/mythtv/mythflix/scripts
%attr(755,root,root) %{_datadir}/mythtv/mythflix/scripts/netflix.pl
%{_datadir}/mythtv/netflix_menu.xml
%{_datadir}/mythtv/themes/default/title_netflix.png
%{_datadir}/mythtv/themes/default/netflix-ui.xml
# DUPLICATE WITH MYTHNEWS?
%{_datadir}/mythtv/themes/default/news-info-bg.png
%endif

%if %{with mythcontrols}
%files -n mythcontrols -f mythcontrols.lang
%defattr(644,root,root,755)
%doc mythcontrols/{AUTHORS,README,TODO}
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythcontrols.so
%{_datadir}/mythtv/themes/default/controls-ui.xml
%{_datadir}/mythtv/themes/default/kb-button-off.png
%{_datadir}/mythtv/themes/default/kb-button-on.png
%endif
