%global octpkg fits

Summary:	Functions for reading, and writing FITS file with Octave
Name:		octave-fits
Version:	1.0.7
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/fits/
Source0:	https://downloads.sourceforge.net/octave/fits-%{version}.tar.gz
# (debian)
Patch1:		d-nint-fix.patch

BuildRequires:  octave-devel >= 3.0.0
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Octave-FITS package provides functions for reading, and writing
FITS (Flexible Image Transport System) files.

This package uses the libcfitsio library.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

