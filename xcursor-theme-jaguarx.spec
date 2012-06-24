%define		_name jaguarx
Summary:	X11 cursor theme - jaguarx
Summary(pl):	Motyw kursor�w dla X11 - jaguarx
Name:		xcursor-theme-%{_name}
Version:	1.0
Release:	1
License:	Artistic 2.0
Group:		Themes
Source0:	http://www.kde-look.org/content/files/6679-%{_name}.tar.bz2
# Source0-md5:	02aa1e61363a5940ae952a64dc098d71
URL:		http://www.kde-look.org/content/show.php?content=6679
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This theme consists of a black pointer cursor and other colorful
cursors. They look like the default X11 theme with a smooth drop
shadow. The color wheel makes it fit nicely into more colorful themes
while maintaining a serious look.

%description -l pl
Ten motyw sk�ada si� z czarnego kursora wskazuj�cego oraz pozosta�ych
kolorowych kursor�w. Wsp�lnie przypominaj� domy�lny motyw X11 z
dodanym cieniem. Kolorowe ko�o, b�d�ce elementem motywu, sprawia, �e
pasuje on r�wnie� do bardziej kolorowych styli, nie trac�c przy tym
powa�nego wygl�du.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
cp -df cursors/*  $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}
