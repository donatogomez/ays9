
@0x886cc4c01082ae4d;
struct Schema {
	hostNode @0 :Text;
	flist @1 :Text = "https://stor.jumpscale.org/stor2/flist/aysbuild/jumpscale.flist";
	dnsSshkey @2 :Text;
	domain @3 :Text;
	botClient @4 :Text;
	botSecret @5 :Text;
	oauthOrganization @6 :Text;
	oauthClientId @7 :Text;
	oauthClientSecret @8 :Text;
	oauthJwtKey @9 :Text;
	caddyEmail @10 :Text;
	caddyStagging @11 :Bool = false;

}
