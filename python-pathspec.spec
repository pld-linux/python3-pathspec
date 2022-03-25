#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Utility library for gitignore style pattern matching of file paths
Summary(pl.UTF-8):	Biblioteka narzędzioawa do dopasowywania wzorców ścieżek plików w stylu gitignore
Name:		python-pathspec
Version:	0.9.0
Release:	2
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathspec/
Source0:	https://files.pythonhosted.org/packages/source/p/pathspec/pathspec-%{version}.tar.gz
# Source0-md5:	9b6b70fa5ffc31e6f5700522880140c0
URL:		https://pypi.org/project/pathspec/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-pathspec
Summary:	Utility library for gitignore style pattern matching of file paths
Summary(pl.UTF-8):	Biblioteka narzędzioawa do dopasowywania wzorców ścieżek plików w stylu gitignore
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pathspec
pathspec is a utility library for pattern matching of file paths. So
far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its
gitignore files.

%description -n python3-pathspec -l pl.UTF-8
pathspec to biblioteka narzędziowa do dopasowywania wzorców ścieżek
plików. Obecnie obejmuje to tylko algorytm dopasowywania wildmatch
Gita, wywodzący się z wildmatch programu Rsync. Git wykorzystuje
wildmatch na potrzeby plików gitignore.

%prep
%setup -q -n pathspec-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s pathspec/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s pathspec/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pathspec/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pathspec/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/pathspec
%{py_sitescriptdir}/pathspec-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pathspec
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/pathspec
%{py3_sitescriptdir}/pathspec-%{version}-py*.egg-info
%endif
