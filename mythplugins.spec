# disable mythmusic,mythphone due to https://bugs.pld-linux.org/?do=details&id=5687
%bcond_with	mythmusic
%bcond_with mythphone
#
Summary:	Main MythTV plugins.
Name:		mythplugins
Version:	0.18.1
Release:	0.112.3
License:	GPL v2
Group:		Applications/Multimedia
URL:		http://www.mythtv.org/
Source0:	http://www.mythtv.org/mc/%{name}-%{version}.tar.bz2
# Source0-md5:	1d94d19e2a13c24a408ced9b6c4f5b47
Patch0:		%{name}-configure.patch
BuildRequires:	SDL-devel
BuildRequires:	X11-OpenGL-devel
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
BuildRequires:	transcode >= 0.6.8
BuildRequires:	xvid-devel >= 1:0.9.1
BuildRequires:	zlib-devel
Requires:	mythbrowser
Requires:	mythdvd
Requires:	mythgallery
Requires:	mythgame
%{?with_mythmusic:Requires:	mythmusic}
Requires:	mythnews
%{?with_mythphone:Requires:	mythphone}
Requires:	mythvideo
Requires:	mythweather
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		api_ver %(echo %{version} | cut -d. -f1,2)

%description
This is a consolidation of all the official MythTV plugins that used
to be distributed as separate downloads from mythtv.org.

%package -n mythmusic
Summary:	The music player add-on module for MythTV.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythmusic
Music add-on for mythtv.

%package -n mythvideo
Summary:	A generic video player frontend module for MythTV.
Group:		Applications/Multimedia
Requires:	mplayer
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythvideo
A generic video player frontend module for MythTV.

%package -n mythweather
Summary:	A MythTV module that displays a weather forcast.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythweather
A MythTV module that displays a weather forcast.

%package -n mythgallery
Summary:	A gallery/slideshow module for MythTV.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythgallery
A gallery/slideshow module for MythTV.

%package -n mythgame
Summary:	A game frontend (xmame, nes, snes, pc) for MythTV.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythgame
A game frontend (xmame, nes, snes, pc) for MythTV.

%package -n mythdvd
Summary:	A DVD player module for MythTV.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}
Requires:	transcode >= 0.6.8

%description -n mythdvd
MythDVD is a MythTV module that allows you to play DVD's on a myth-box
and (optionally) rip DVD's and transcode their video and audio content
to other (generally smaller) formats. The playing features are simply
myth-style wrappers for your favourite DVD playing software (mplayer,
ogle, xine, etc). The transcoding is based on and derived from the
excellent transcode package.

%package -n mythnews
Summary:	A RSS News Feed Plugin for MythTV.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythnews

%package -n mythbrowser
Summary:	A small web browser module for MythTV.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythbrowser
MythBrowser is a full fledged web-browser (multiple tabs) to display
webpages in full-screen mode. Simple page navigation is possible.
Starting with version 0.13 it also has full support for mouse driven
navigation (right mouse opens and clos es the popup menu).

MythBrowser also contains a BookmarkManager to manage the website
links in a simple mythplugin.

%package -n mythphone
Summary:	A video conferencing module for MythTV.
Group:		Applications/Multimedia
Requires:	mythtv-frontend-api = %{api_ver}

%description -n mythphone
Mythphone is a phone and videophone capability on MYTH using the
standard SIP protocol. It is compatible with Microsoft XP Messenger
and with SIP Service Providers such as Free World Dialup
(fwd.pulver.com).

%prep
%setup -q
%patch0 -p1

# lib64 fix
find '(' -name '*.[ch]' -o -name '*.cpp' -o -name '*.pro' ')' | \
xargs grep -l /lib/ . | xargs sed -i -e '
	s,/usr/lib/,/usr/%{_lib}/,g
	s,{PREFIX}/lib,{PREFIX}/%{_lib}/,g
'

# include mythtv build settings
cp %{_datadir}/mythtv/build/config.mak .
sed -i -e '1iinclude(config.mak)'  settings.pro

# Fix /mnt/store -> /var/lib/mythmusic
sed -i -e's|/mnt/store/music|/var/lib/mythmusic|' mythmusic/mythmusic/globalsettings.cpp
# Fix /mnt/store -> /var/lib/mythmusic
sed -i -e's|/share/Movies/dvd|/var/lib/mythvideo|' mythvideo/mythvideo/globalsettings.cpp

%build
export QTDIR="%{_prefix}"
# Not gnu configure
%configure \
	--enable-all \
	--disable-festival \
	%{!?with_mythmusic:--disable-mythmusic} \
	%{!?with_mythphone:--disable-mythphone}

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

%install
rm -rf $RPM_BUILD_ROOT

export QTDIR="%{_prefix}"
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/lib/{mythmusic,mythvideo,pictures}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/nes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/snes/{roms,screens}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/xmame/{roms,screens,flyers,cabs}
install -d $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC/screens
install -d $RPM_BUILD_ROOT%{_datadir}/xmame
ln -s %{_datadir}/xmame $RPM_BUILD_ROOT%{_datadir}/mythtv/games/xmame
install -d $RPM_BUILD_ROOT%{_datadir}/xmame/flyers
ln -s snap $RPM_BUILD_ROOT%{_datadir}/xmame/screens

cp -a mythgame/gamelist.xml $RPM_BUILD_ROOT%{_datadir}/mythtv/games/PC/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%if %{with mythmusic}
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
%endif

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
%{_datadir}/mythtv/mythvideo/scripts/README
%{_datadir}/mythtv/mythvideo/scripts/imdb.pl
%{_datadir}/mythtv/mythvideo/scripts/allocine.pl
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
%{_datadir}/xmame/screens
%{_datadir}/xmame/flyers
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

%if %{with mythphone}
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
