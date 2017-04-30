
@0xecdbd5038c7cf72c;
struct Schema {
	os @0 :Text;
	sitename @1 :Text;
	tidb @2 :Text;
	tidbhost @3 :Text = "127.0.0.1";
	tidbuser @4 :Text = "root";
	tidbpassword @5 :Text;
	owncloudAdminUser @6 :Text = "admin";
	owncloudAdminPassword @7 :Text = "admin";

}
