
@0x96b5bdf0526c1bb3;
struct Schema {
	os @0 :Text;
	fs @1 :Text;
	redis @2 :Text;
	listenAddr @3 :Text = "127.0.0.1";
	listenPort @4 :Int64 = 82;
	spaceDefault @5 :Text = "AYS81";
	oauthEnabled @6 :Bool = false;
	oauthClientId @7 :Text;
	oauthScope @8 :Text;
	oauthSecret @9 :Text;
	oauthClientUrl @10 :Text = "https://itsyou.online/v1/oauth/authorize";
	oauthClientUserInfoUrl @11 :Text = "https://itsyou.online/api/users";
	oauthProvider @12 :Text = "itsyou.online";
	oauthDefaultGroups @13 :List(Text);
	oauthOrganization @14 :Text;
	oauthRedirectUrl @15 :Text;
	oauthTokenUrl @16 :Text = "https://itsyou.online/v1/oauth/access_token";

}
