
@0x9de1f58bd6c1b732;
struct Schema {
	os @0 :Text;
	redis @1 :Text;
	fs @2 :Text;
	portal @3 :Text;
	domain @4 :Text;
	oauthClientId @5 :Text;
	oauthClientSecret @6 :Text;
	oauthOrganization @7 :Text;
	oauthRedirectUrl @8 :Text;
	oauthJwtKey @9 :Text;
	apiHost @10 :Text = "localhost";
	apiPort @11 :Int64 = 5000;

}
