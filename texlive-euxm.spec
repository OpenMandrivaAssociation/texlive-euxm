Name:		texlive-euxm
Version:	20111102
Release:	1
Summary:	TeXLive euxm package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euxm.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive euxm package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
