%global tl_name mathabx
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Three series of mathematical symbols
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mathabx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Mathabx is a set of 3 mathematical symbols font series: matha, mathb and
mathx. They are defined by Metafont code and should be of reasonable
quality (bitmap output). Things change from time to time, so there is no
claim of stability (encoding, metrics, design). The package includes
Plain TeX and LaTeX support macros. A version of the fonts, in Adobe
Type 1 format, is also available.

