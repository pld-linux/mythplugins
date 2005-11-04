#
# Conditional build:
%bcond_without	binary		# skip binary plugins (build only mythweb)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Main MythTV plugins
Summary(pl):	G³ówne wtyczki MythTV
Name:		mythplugins
Version:	0.18.1
%define	_snap 20051104
%define	_rel 0.5
Release:	0.113.%{_snap}.%{_rel}
License:	GPL v2
Group:		Applications/Multimedia
#Source0:	http://www.mythtv.org/mc/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	021633295bdcc34f31580239cb0b1074
Source1:	mythweb.conf
#Patch0:		%{name}-configure.patch
#Patch1:		%{name}-libversion.patch
Patch2:		%{name}-lib64.patch
Patch3:		%{name}-paths.patch
Patch4:		mythweb-config.patch
URL:		http://www.mythtv.org/
%if %{with binary}
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	a52dec-libs-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	faad2-devel >= 2.0-5.2
BuildRequires:	fftw-devel >= 2.1.3
BuildRequires:	flac-devel >= 1.0.4
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libcdaudio-devel
BuildRequires:	libdvdcss-devel >= 1.2.7
BuildRequires:	libdvdread-devel >= 0.9.4
BuildRequires:	libexif-devel
BuildRequires:	libfame-devel >= 0.9.0
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmyth-devel >= 0.18.1-0.21
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	mjpegtools-devel >= 1.6.1
BuildRequires:	nasm
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRequires:	transcode >= 0.6.8
BuildRequires:	xvid-devel >= 1:0.9.1
BuildRequires:	zlib-devel
%endif
Requires:	mythbrowser
Requires:	mythdvd
Requires:	mythgallery
Requires:	mythgame
Requires:	mythmusic
Requires:	mythnews
Requires:	mythphone
Requires:	mythvideo
Requires:	mythweather
Requires:	mythweb
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		api_ver %(echo %{version} | cut -d. -f1,2)

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
Requires:	apache >= 1.3.33-2
Requires:	php >= 3:4.2.2
Requires:	php-mysql >= 3:4.2.2

%description -n mythweb
The web interface to MythTV.

%description -n mythweb -l pl
Interfejs WWW do MythTV.

%prep
%setup -q %{?_snap:-n %{name}}
#%patch0 -p1
#%patch1 -p1
%if %{_lib} != "lib"
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1

# trash
rm mythweb/themes/compact.tar.bz2
rm mythweb/images/icons/.cvsignore

%if %{with binary}
# include mythtv build settings
cp %{_datadir}/mythtv/build/config.mak .
sed -i -e "1iinclude(`pwd`/config.mak)"  settings.pro

%ifarch %{x8664}
	# mmx asm isn't x86_64 compatible in mythmusic
	echo 'DEFINES -= HAVE_MMX' >> settings.pro
%endif
%endif

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
	--disable-festival

#	--enable-opengl          enable OpenGL (Music and Gallery) [default=no]
#	--enable-transcode       enable DVD ripping and transcoding [default=no]
#	--enable-vcd             enable VCD playing [default=no]
#	--enable-exif            enable reading of EXIF headers [default=no]
#	--enable-fftw            enable fftw visualizers [default=no]
#	--enable-sdl             use SDL for the synaesthesia output [default=no]
#	--enable-aac             enable AAC/MP4 audio file decompression [default=no]
#	--enable-festival        enable festival TTS Engine [default=no]

qmake mythplugins.pro
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with binary}
export QTDIR="%{_prefix}"
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/lib/{mythmusic,mythvideo,pictures}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/nes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/snes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/xmame/{roms,screens,flyers,cabs}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC/screens
cp -a mythgame/gamelist.xml $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC
%endif

# mythweb
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/mythweb,%{_datadir}/mythweb/{includes,languages},/var/cache/mythweb/{image_cache,php_sessions}}
cp -a mythweb/*.{html,php} $RPM_BUILD_ROOT%{_datadir}/mythweb
cp -a mythweb/languages/*.php $RPM_BUILD_ROOT%{_datadir}/mythweb/languages
cp -a mythweb/includes/*.php $RPM_BUILD_ROOT%{_datadir}/mythweb/includes
cp -a mythweb/{images,js,themes,templates,vxml} $RPM_BUILD_ROOT%{_datadir}/mythweb
cp -a mythweb/config/*.{php,dat} $RPM_BUILD_ROOT%{_sysconfdir}/mythweb
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mythweb/apache.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/mythweb/htpasswd

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -n mythweb -- apache1 >= 1.3.33-2
%apache_config_install -v 1 -c %{_sysconfdir}/mythweb/apache.conf
exit 0

%triggerun -n mythweb -- apache1 >= 1.3.33-2
%apache_config_uninstall -v 1
exit 0

%triggerin -n mythweb -- apache >= 2.0.0
%apache_config_install -v 2 -c %{_sysconfdir}/mythweb/apache.conf
exit 0

%triggerun -n mythweb -- apache >= 2.0.0
%apache_config_uninstall -v 2
exit 0

%files
%defattr(644,root,root,755)

%if %{with binary}
%files -n mythmusic
%defattr(644,root,root,755)
%doc mythmusic/README mythmusic/UPGRADING mythmusic/AUTHORS mythmusic/musicdb
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythmusic.so
/var/lib/mythmusic
%{_datadir}/mythtv/musicmenu.xml
%{_datadir}/mythtv/music_settings.xml
%{_datadir}/mythtv/i18n/mythmusic_*.qm
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
%{_datadir}/mythtv/themes/default/music-ui.xml
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

%files -n mythvideo
%defattr(644,root,root,755)
%doc mythvideo/README mythvideo/UPGRADING mythvideo/videodb
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythvideo.so
%{_datadir}/mythtv/i18n/mythvideo_*.qm
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
/var/lib/mythvideo

%files -n mythweather
%defattr(644,root,root,755)
%doc mythweather/README
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythweather.so
%{_datadir}/mythtv/i18n/mythweather_*.qm
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

%files -n mythgallery
%defattr(644,root,root,755)
%doc mythgallery/README mythgallery/UPGRADING
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgallery.so
%{_datadir}/mythtv/themes/default/gallery-ui.xml
%{_datadir}/mythtv/themes/default/gallery-*.png
%{_datadir}/mythtv/i18n/mythgallery_*.qm
/var/lib/pictures

%files -n mythgame
%defattr(644,root,root,755)
%doc mythgame/README mythgame/UPGRADING
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythgame.so
%{_datadir}/mythtv/games
#%config %{_datadir}/mythtv/games/PC/gamelist.xml
#%{_datadir}/xmame/screens
#%{_datadir}/xmame/flyers
%{_datadir}/mythtv/game_settings.xml
%{_datadir}/mythtv/themes/default/game-ui.xml
%{_datadir}/mythtv/i18n/mythgame_*.qm

%files -n mythdvd
%defattr(644,root,root,755)
%doc mythdvd/README mythdvd/UPGRADING mythdvd/AUTHORS
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythdvd.so
%{_datadir}/mythtv/dvd_settings.xml
%{_datadir}/mythtv/dvdmenu.xml
%{_datadir}/mythtv/themes/default/dvd-ui.xml
%{_datadir}/mythtv/themes/default/md_*.png
%{_datadir}/mythtv/i18n/mythdvd_*.qm
%attr(755,root,root) %{_bindir}/mtd

%files -n mythnews
%defattr(644,root,root,755)
%doc mythnews/README mythnews/AUTHORS
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythnews.so
%{_datadir}/mythtv/mythnews
%{_datadir}/mythtv/themes/default/news-ui.xml
%{_datadir}/mythtv/themes/default/news-info-bg.png
%{_datadir}/mythtv/i18n/mythnews_*.qm

%files -n mythbrowser
%defattr(644,root,root,755)
%doc mythbrowser/README mythbrowser/AUTHORS
%attr(755,root,root) %{_bindir}/mythbrowser
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythbookmarkmanager.so
%{_datadir}/mythtv/themes/default/webpage.png
%{_datadir}/mythtv/i18n/mythbrowser_*.qm

%files -n mythphone
%defattr(644,root,root,755)
%doc mythphone/README mythphone/AUTHORS mythphone/TODO
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythphone.so
%{_datadir}/mythtv/themes/default/phone-ui.xml
%{_datadir}/mythtv/themes/default/webcam-ui.xml
%{_datadir}/mythtv/themes/default/mp_*.png
%{_datadir}/mythtv/themes/default/phone.png
%{_datadir}/mythtv/i18n/mythphone_*.qm
%endif

%files -n mythweb
%defattr(644,root,root,755)
%doc mythweb/{README,TODO} mythweb/languages/*.{pl,txt}
%attr(750,root,http) %dir %{_sysconfdir}/mythweb
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mythweb/apache.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mythweb/*.php
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mythweb/*.dat
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mythweb/htpasswd
%{_datadir}/mythweb
%dir /var/cache/mythweb
%dir %attr(771,root,http) /var/cache/mythweb/image_cache
%dir %attr(771,root,http) /var/cache/mythweb/php_sessions
