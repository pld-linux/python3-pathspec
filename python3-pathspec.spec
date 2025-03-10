#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Utility library for gitignore style pattern matching of file paths
Summary(pl.UTF-8):	Biblioteka narzędzioawa do dopasowywania wzorców ścieżek plików w stylu gitignore
Name:		python3-pathspec
Version:	0.12.1
Release:	2
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathspec/
Source0:	https://pypi.debian.net/pathspec/pathspec-%{version}.tar.gz
# Source0-md5:	2b26ad1981bfa23748e115f00085624c
URL:		https://pypi.org/project/pathspec/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pathspec is a utility library for pattern matching of file paths. So
far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its
gitignore files.

%description -l pl.UTF-8
pathspec to biblioteka narzędziowa do dopasowywania wzorców ścieżek
plików. Obecnie obejmuje to tylko algorytm dopasowywania wildmatch
Gita, wywodzący się z wildmatch programu Rsync. Git wykorzystuje
wildmatch na potrzeby plików gitignore.

%prep
%setup -q -n pathspec-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/pathspec
%{py3_sitescriptdir}/pathspec-%{version}.dist-info
