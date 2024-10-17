Name:		texlive-dtxtut
Version:	69587
Release:	1
Summary:	Tutorial on writing .dtx and .ins files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/dtxtut
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxtut.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxtut.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
