
@0x948837c6862de1f0;
struct Schema {
	sshkey @0 :Text;
	client @1 :Text;
	projectName @2 :Text;
	planType @3 :Text = "Type 0";
	deviceName @4 :Text;
	deviceOs @5 :Text = "Ubuntu 14.04 LTS";
	deviceId @6 :Text;
	location @7 :Text = "amsterdam";
	ipPublic @8 :Text;
	ports @9 :List(Text);
	sshLogin @10 :Text;
	sshPassword @11 :Text;
	ipxeScriptUrl @12: Text;
}
