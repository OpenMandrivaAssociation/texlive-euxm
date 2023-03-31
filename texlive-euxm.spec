Name:		texlive-euxm
Version:	54074
Release:	2
Summary:	TeXLive euxm package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euxm.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive euxm package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/euxm/eubase.mf
%{_texmfdistdir}/fonts/source/public/euxm/eusmch.mf
%{_texmfdistdir}/fonts/source/public/euxm/euxm10.mf
%{_texmfdistdir}/fonts/source/public/euxm/euxm5.mf
%{_texmfdistdir}/fonts/source/public/euxm/euxm7.mf
%{_texmfdistdir}/fonts/source/public/euxm/euxmch.mf
%{_texmfdistdir}/fonts/tfm/public/euxm/euxm10.tfm
%{_texmfdistdir}/fonts/tfm/public/euxm/euxm5.tfm
%{_texmfdistdir}/fonts/tfm/public/euxm/euxm7.tfm

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
