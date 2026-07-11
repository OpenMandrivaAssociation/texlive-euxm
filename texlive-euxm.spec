%global tl_name euxm
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	extended Euler by DEK
Group:		Publishing
URL:		https://www.ctan.org/pkg/euxm
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euxm.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Includes two additional characters needed for Concrete Math (ca. 1991).

