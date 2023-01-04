resource "google_compute_firewall" "allow-traffic" {
  name    = "test-firewall"
  network = google_compute_network.vpc-network-team3.name

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "22", "3306"]
  }
  source_tags   = ["akshayapp_server-firewall"]
  source_ranges = ["0.0.0.0/0"]
}


# Note here that in thr line number 5 I am allowing icmp so that , allows ingress, or inbound, ICMP traffic from any source to any instance on the network.
