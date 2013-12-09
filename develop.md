How to Develop and Contribute to rpcalc
=======================================

This project uses the [successful git branching model](http://nvie.com/posts/a-successful-git-branching-model/) and sticks closely to [semantic versioning](http://semver.org/).

## Prepare a Release/Hotfix Branch
- Branch off develop _e.g._ `git checkout develop && git checkout -b hotfix-0.3.1`
- Delete develop.md
- Bump version number in setup.py and rpcalc.py
- Make sure that no `## __NEXT RELEASE__` section exists in `changelog.md`.
- Commit and push. `git commit -am 'readied hotfix 0.3.1' && git push`

## Releasing

After a release or hotfix branch is prepared, the following tasks will properly release the next version.

**Remember to force `git merge` not to fast forward!**

- Merge changes to master _e.g._ `git checkout master && git merge --no-ff hotfix-0.3.1`.
- Tag the release on master. Use an annotated tag with the name `v` followed by the semantic version number _e.g._ `git tag -a v0.3.1 -m 'squashes trig bugs'`.
- Push. `git push`
- Merge changes to develop _e.g._ `git checkout develop && git merge --no-ff hotfix-0.3.1`.
- Prepare develop for further development _e.g._ `git checkout origin/develop develop.md`; add `## __NEXT RELEASE__` to changelog.md
- Commit and push. `git commit -am 'readied for further development' && git push`
- Delete the release/hotfix branch locally and remotely _e.g._ `git branch -d hotfix-0.3.1` `git push origin :hotfix-0.3.1`
- Push with `git push` and `git push --tags`.
- Write some release notes in [the releases section](https://github.com/qguv/rpcalc/releases) on GitHub. Flag a pre-release if it is necessary.
- Go to the [GitHub page generator](https://github.com/qguv/rpcalc/generated_pages/new), hit _Load README.md_. Hit _Continue to Layouts_, choose the _Leap Day_ theme, and hit _Publish_.
- [update](https://github.com/qguv/pkgbuilds/edit/master/rpcalc/PKGBUILD) PKGBUILD if necessary
- burp upload PKGBUILD with `burp -u qguv -c science rpc<Tab>`
