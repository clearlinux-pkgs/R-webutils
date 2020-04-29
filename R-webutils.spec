#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-webutils
Version  : 1.1
Release  : 17
URL      : https://cran.r-project.org/src/contrib/webutils_1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/webutils_1.1.tar.gz
Summary  : Utility Functions for Developing Web Applications
Group    : Development/Tools
License  : MIT
Requires: R-webutils-lib = %{version}-%{release}
Requires: R-curl
Requires: R-jsonlite
BuildRequires : R-curl
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
or application/x-www-form-urlencoded format. Includes example of hosting
    and parsing html form data in R using either 'httpuv' or 'Rhttpd'.

%package lib
Summary: lib components for the R-webutils package.
Group: Libraries

%description lib
lib components for the R-webutils package.


%prep
%setup -q -c -n webutils

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588191164

%install
export SOURCE_DATE_EPOCH=1588191164
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webutils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webutils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webutils
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc webutils || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/webutils/DESCRIPTION
/usr/lib64/R/library/webutils/INDEX
/usr/lib64/R/library/webutils/LICENSE
/usr/lib64/R/library/webutils/Meta/Rd.rds
/usr/lib64/R/library/webutils/Meta/features.rds
/usr/lib64/R/library/webutils/Meta/hsearch.rds
/usr/lib64/R/library/webutils/Meta/links.rds
/usr/lib64/R/library/webutils/Meta/nsInfo.rds
/usr/lib64/R/library/webutils/Meta/package.rds
/usr/lib64/R/library/webutils/NAMESPACE
/usr/lib64/R/library/webutils/NEWS
/usr/lib64/R/library/webutils/R/webutils
/usr/lib64/R/library/webutils/R/webutils.rdb
/usr/lib64/R/library/webutils/R/webutils.rdx
/usr/lib64/R/library/webutils/help/AnIndex
/usr/lib64/R/library/webutils/help/aliases.rds
/usr/lib64/R/library/webutils/help/paths.rds
/usr/lib64/R/library/webutils/help/webutils.rdb
/usr/lib64/R/library/webutils/help/webutils.rdx
/usr/lib64/R/library/webutils/html/00Index.html
/usr/lib64/R/library/webutils/html/R.css
/usr/lib64/R/library/webutils/testpage.html
/usr/lib64/R/library/webutils/tests/testthat.R
/usr/lib64/R/library/webutils/tests/testthat/description.orig
/usr/lib64/R/library/webutils/tests/testthat/iris.orig
/usr/lib64/R/library/webutils/tests/testthat/logo.orig
/usr/lib64/R/library/webutils/tests/testthat/posttypes
/usr/lib64/R/library/webutils/tests/testthat/test-echo.R
/usr/lib64/R/library/webutils/tests/testthat/test-encoding.R
/usr/lib64/R/library/webutils/tests/testthat/test-parse.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/webutils/libs/webutils.so
