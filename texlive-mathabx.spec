Name:		texlive-mathabx
Version:	20080915
Release:	1
Summary:	Three series of mathematical symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/mathabx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Mathabx is a set of 3 mathematical symbols font series: matha,
mathb and mathx. They are defined by MetaFont code and should
be of reasonable quality (bitmap output). Things change from
time to time, so there is no claim of stability (encoding,
metrics, design). The package includes Plain TeX and LaTeX
support macros.

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
%{_texmfdistdir}/fonts/source/public/mathabx/matha10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha12.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha5.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha6.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha7.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha8.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha9.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathacnt.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathadrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matharrw.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathastr.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathastrotest10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathastrotestdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathasym.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb12.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb5.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb6.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb7.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb8.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb9.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbase.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbdel.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbigs.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbsym.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathc10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathcall.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathcallgreek.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathcdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathfine.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathgrey.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathhbrw.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathineq.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathltlk.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathmbcb.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathprmt.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathsmsy.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathsubs.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathsymb.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathu10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathudrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathusym.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathux10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathuxdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx12.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx5.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx6.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx7.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx8.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx9.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathxdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/maydigit.mf
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha12.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha9.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathastrotest10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb12.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb9.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathc10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathu10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathux10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx12.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx9.tfm
%{_texmfdistdir}/tex/generic/mathabx/mathabx.dcl
%{_texmfdistdir}/tex/generic/mathabx/mathabx.sty
%{_texmfdistdir}/tex/generic/mathabx/mathabx.tex
%doc %{_texmfdistdir}/doc/fonts/mathabx/README
%doc %{_texmfdistdir}/doc/fonts/mathabx/mathtest.pdf
%doc %{_texmfdistdir}/doc/fonts/mathabx/mathtest.tex
%doc %{_texmfdistdir}/doc/fonts/mathabx/testmac.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
