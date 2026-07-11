%global tl_name dtxtut
%global tl_revision 69587

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Tutorial on writing .dtx and .ins files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/dtxtut
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxtut.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxtut.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This tutorial is intended for advanced LaTeX2e users who want to learn
how to create .ins and .dtx files for distributing their homebrewed
classes and package files.

