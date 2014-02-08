# revision 20202
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-euxm
Version:	20111103
Release:	3
Summary:	TeXLive euxm package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euxm.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 751668
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718391
- texlive-euxm
- texlive-euxm
- texlive-euxm
- texlive-euxm

