
@0xcfb21e2a3d7e8f2b;
struct Schema {
	os @0 :Text;
	fs @1 :Text;
	botToken @2 :Text;
	oauthHost @3 :Text = "0.0.0.0";
	oauthPort @4 :Int64 = 6366;
	oauthRedirect @5 :Text;
	oauthClient @6 :Text;
	oauthSecret @7 :Text;
	oauthItsyouonlinehost @8 :Text = "https://itsyou.online";

}
