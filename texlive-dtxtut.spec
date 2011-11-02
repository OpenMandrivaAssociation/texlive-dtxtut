Name:		texlive-dtxtut
Version:	20070201
Release:	1
Summary:	Tutorial on writing .dtx and .ins files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/dtxtut
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxtut.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxtut.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This tutorial is intended for advanced LaTeX2e users who want
to learn how to create .ins and .dtx files for distributing
their homebrewed classes and style files.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/dtxtut/README
%doc %{_texmfdistdir}/doc/latex/dtxtut/cskeleton.dtx
%doc %{_texmfdistdir}/doc/latex/dtxtut/cskeleton.ins
%doc %{_texmfdistdir}/doc/latex/dtxtut/dtxtut.pdf
%doc %{_texmfdistdir}/doc/latex/dtxtut/dtxtut.tex
%doc %{_texmfdistdir}/doc/latex/dtxtut/skeleton.dtx
%doc %{_texmfdistdir}/doc/latex/dtxtut/skeleton.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
